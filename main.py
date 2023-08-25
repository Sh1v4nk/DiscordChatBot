# Import necessary libraries
import discord 
import os
import openai
import difflib  # Import the difflib module for text similarity comparison
import json

# Read environment variables from config.json
with open('config.json') as config_file:
    config_data = json.load(config_file)

# Get the secret key and API key
my_secret = config_data['PassKey']
openai.api_key = config_data['OPENAI_API_KEY']


# Initialize an empty list to store chat history
chat_history = []

# Initialize a variable to store the previous response
prev_response = ""

# Define a class for the Discord bot
class MyClient(discord.Client):

    # This method is called when the bot successfully logs in
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    # This method is called whenever a message is sent in a server the bot is a part of
    async def on_message(self, message):
        global chat_history
        global prev_response

        # Check if the message sender is not the bot itself
        if self.user != message.author:
            # Check if the bot is mentioned in the message
            if self.user in message.mentions:
                author = message.author.name  # Get the name of the message sender
                content = message.content  # Get the content of the message

                # Update chat history with the latest message
                chat_history.append(f"Message from {author}: {content}")

                # Define a maximum limit for the chat history
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
                prev_response = message_to_send  # Update the previous response

                # Send the generated response as a reply to the triggering message
                await message.reply(message_to_send, mention_author=False)

# Define the intents the bot should listen to
intents = discord.Intents.default()
intents.message_content = True

# Create an instance of the bot with specified intents
client = MyClient(intents=intents)

# Run the bot using the provided token
client.run(my_secret)
