import discord 
import os
import openai
import difflib
import json
import requests

with open('config.json') as config_file:
    config_data = json.load(config_file)

my_secret = config_data['PassKey']
openai.api_key = config_data['OPENAI_API_KEY']


chat_history = []
prev_response = ""

# Define a class for the Discord bot
class MyClient(discord.Client):

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        global chat_history
        global prev_response

        if self.user != message.author:
            # Check if the bot is mentioned in the message
            if self.user in message.mentions:
                author = message.author.name
                content = message.content

                # Update chat history with the latest message
                chat_history.append(f"Message from {author}: {content}")

                MAX_CHAT_HISTORY = 10
                if len(chat_history) > MAX_CHAT_HISTORY:
                    chat_history = chat_history[-MAX_CHAT_HISTORY:]  # Keep only the most recent messages

                # Create a context by joining the chat history messages
                context = "\n".join(chat_history)

                # Generate a response using OpenAI API
                response = None
                while response is None or difflib.SequenceMatcher(None, response.choices[0].text, prev_response).ratio() > 0.7:
                    # Build a prompt by combining the context, user input, and bot placeholder
                    prompt = f"Context:\n{context}\nUser: {content}\nChatterBox: "
                    response = openai.Completion.create(
                        model="text-davinci-003", # Specify the model to use (GPT-3)
                        prompt=prompt,
                        temperature=0.7,
                        max_tokens=256,
                        top_p=1,
                        frequency_penalty=0.2,
                        presence_penalty=0.5,
                    )

                message_to_send = response.choices[0].text
                prev_response = message_to_send

                await message.reply(message_to_send, mention_author=False)

def get_weather(location):
    # Replace with your OpenWeatherMap API key
    api_key = "WeatherKey"
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric",  # Use "imperial" for Fahrenheit
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        return f"The weather in {location} is {description} with a temperature of {temperature}°C."
    else:
        return "Unable to fetch weather information."

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

client.run(my_secret)