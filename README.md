<div align="center">

# DiscordChatBot

[![code style: ruff](https://img.shields.io/badge/code_style-Ruff-orange?style=flat-square&logoColor=black)](https://github.com/astral-sh/ruff)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
![GitHub repo size](https://img.shields.io/github/repo-size/Sh1v4nk/DiscordChatBot)

Welcome to the repository for my DiscordChatBot project, powered by the OpenAI API. This project utilizes Python to create a chatbot that can engage in conversations on Discord servers using the OpenAI API. The chatbot leverages the capabilities of GPT-3.5 to generate human-like responses, making interactions with users more dynamic and engaging.

</div>

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
  - [Application Demo](#application-demo)
- [Technology Used](#technology-used)
- [Get API Keys](#get-api-keys)
- [Installation](#installation)
- [Running the Bot](#running-the-bot)
- [Invite the Bot](#invite-the-bot)
- [Usage](#usage)
- [Customization](#customization)
- [Further Exploration](#further-exploration)
- [Disclaimer](#disclaimer)
- [Contributing](#contributing)
- [License](#license)

## Overview

Welcome to the DiscordChatBot project powered by the OpenAI API! 🤖🚀

This project demonstrates a Python-based chatbot designed to converse within Discord servers. By harnessing the capabilities of OpenAI's text-davinci-003 GPT-3.5 model, the chatbot produces contextually fitting and human-like responses, enhancing user interactions with dynamic conversations.

## Key Features

- **Discord Bot Integration:** This code provides a Discord bot implementation that interacts with users in a Discord server, responding to mentions of the bot and facilitating conversations within the Discord environment.

- **OpenAI Integration:** Leveraging the GPT-3 model ("text-davinci-003"), the bot uses the OpenAI API to generate coherent responses that match the conversation context and user input.

- **Chat History Management:** To maintain context, the bot stores a history of recent user messages and responses. This contextual history enhances the relevance of generated replies while managing memory efficiently.

- **Message Similarity Handling:** To prevent repetition, the code employs the `difflib` library to manage similarity between consecutive responses. If a response becomes too similar to the previous one, the bot generates a fresh reply.

- **Dynamic Response Generation:** By combining user messages, chat history, and a predefined bot placeholder, the bot dynamically generates responses that are contextually relevant and engaging.

- **Customizable Prompt Building:** The code constructs prompts that include chat history, user input, and bot placeholders. This approach ensures responses are coherent and context-aware.

- **Token Management:** Responses are kept concise and within OpenAI token limits (`max_tokens=256`), enabling the bot to generate succinct yet meaningful replies.

- **Discord API Interaction:** The bot is built using the Discord.py library, leveraging asynchronous features to handle message events and ensure seamless interactions within the Discord server.

This project offers a unique opportunity to explore the fusion of AI-driven conversation with Discord's dynamic platform. Feel free to dive in, customize prompts, and watch your bot engage in lifelike discussions within your Discord community.

### Application Demo:

<img width="auto" src="https://i.ibb.co/JHhbRqb/image.png" alt="DiscordChatBot Demo">

## Technology Used

This project makes use of the following technologies, libraries, and tools:

- **[Python](https://www.python.org/):** The core programming language used for implementing the chatbot and its interactions.

- **[Discord.py](https://discordpy.readthedocs.io/en/stable/):** A Python library for interacting with the Discord API, enabling the creation of the chatbot and its integration within Discord servers.

- **[OpenAI API](https://openai.com/api/):** The project utilizes the OpenAI API to access the GPT-3.5 model, allowing the chatbot to generate human-like responses.

- **difflib Library:** Used for managing message similarity and generating diverse responses to prevent repetition.

- **JSON:** The configuration for the bot's credentials is stored in JSON format.

These technologies collectively power the chatbot's functionality, integration, and AI-driven interactions within Discord servers.

## Get API Keys

- Obtain a Discord bot token by creating a new bot application within the Discord Developer Portal.

- Get an OpenAI API key by signing up on the OpenAI website.

## Installation

To get started with the DiscordChatbot project, follow these steps:

1. Clone the repository to your local machine:

```bash
git clone https://github.com/Sh1v4nk/DiscordChatBot.git
```

2. Navigate to the project directory:

```bash
cd DiscordChatBot
```

3. Create a new file in the root directory of the project and name it config.json.

4. Inside the .env file, add your Discord bot token and OpenAI API key in the format given in .env.example


**Replace YOUR_DISCORD_BOT_TOKEN with your actual Discord bot token and YOUR_OPENAI_API_KEY with your actual OpenAI API key.**

> ⚠️ **_Note: Keep this file secure and never share it publicly or commit it to version control._**

5. Save and close the .env file.

6. Run the bot using the provided code, and it will use the keys you've provided in the .env file to connect to Discord and use the OpenAI API.

## Running the Bot

_To run the bot, make sure you have Python and the required libraries installed. You can install the required libraries using the following command:_

```
pip install discord.py openai python-dotenv
```

After installing the required libraries, run the bot using the provided code:

```bash
python main.py
```

> ⚠️ **_Note: You can Replace main.py with the actual name of your bot script._**

By following these instructions, you'll be able to set up and run the chatbot with your own API keys. This approach ensures the security of your sensitive information.

## Invite the Bot

1. Go to the Discord Developer Portal and select your bot application.

2. In the "OAuth2" section, choose the "URL Generator" option. Then, place a checkmark next to "bot" in the Scopes section. For access permissions, I recommend selecting "Read Messages/View Channels."

3. Copy the generated OAuth2 URL and paste it into your browser. Choose a server to invite the bot.

## Usage

- Mention the bot in a message to initiate a conversation.

- The bot will reply with a generated response based on the conversation history.

- The conversation history is limited to the last 10 messages.

- The bot uses the OpenAI GPT-3 language model to generate responses.

## Customization

You can customize the behavior of the ChatterBox bot by adjusting various parameters in the `main.py` script:

- **GPT-3 Model Settings:** You can modify the parameters used when making API calls to the GPT-3 model. These parameters include `temperature`, `max_tokens`, `top_p`, `frequency_penalty`, and `presence_penalty`. Adjusting these parameters can influence the creativity and style of the bot's responses. Refer to the [OpenAI API documentation](https://platform.openai.com/docs/api-reference/completions) for more details.

- **Response Criteria:** The `difflib.SequenceMatcher` ratio is used to compare the similarity between the current response and the previous response. You can adjust the threshold value (`0.7` in the provided code) to control when the bot considers a response to be too similar to the previous one and generates a new one.

- **Chat History Length:** The `MAX_CHAT_HISTORY` variable controls the maximum number of messages stored in the chat history. You can adjust this value to increase or decrease the context that the bot uses for generating responses.

## Further Exploration

For more information about customizing the GPT-3 model behavior, experimentation with different prompts, and utilizing additional features, refer to the official [OpenAI API documentation](https://platform.openai.com/docs/api-reference/introduction) and [Guides](https://platform.openai.com/docs/guides/gpt).

Please keep in mind that fine-tuning the bot's behavior requires a good understanding of both the OpenAI API and the bot's code implementation.

## Disclaimer

ChatterBox is a simple example of a Discord bot using the OpenAI API. The bot's behavior and responses are generated based on the provided code and settings.

## Contributing

Contributions to DiscordChatBot are highly welcome! Please submit a pull request if you have any ideas for new features, enhancements to existing functionality, or if you find any bugs. Your contributions are much appreciated and will help to improve the overall user experience.

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and submit a pull request.

> "Alone we can do so little; together we can do so much." - Helen Keller

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Sh1v4nk/DiscordChatBot/blob/main/LICENSE) file for details.

---

Thank you for visiting my DiscordChatBot repository. If you have any suggestions or feedback, feel free to reach out to me.

Connect with me:

<div align="center">
  <a href="mailto:shivankpandey113@gmail.com" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Gmail&logo=gmail&label=&color=D14836&logoColor=white&labelColor=&style=for-the-badge" height="30" alt="gmail logo"  />
  </a>
  <a href="https://twitter.com/sh1v4nk" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Twitter&logo=twitter&label=&color=1DA1F2&logoColor=white&labelColor=&style=for-the-badge" height="30" alt="twitter logo"  />
  </a>
    <a href="https://www.linkedin.com/in/sh1v4nk/" target="_blank">
    <img src="https://img.shields.io/static/v1?message=LinkedIn&logo=linkedin&label=&color=0077B5&logoColor=white&labelColor=&style=for-the-badge" height="30" alt="linkedin logo"  />
  </a>
  <a href="https://www.instagram.com/sh1v4nk_/" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Instagram&logo=instagram&label=&color=E4405F&logoColor=white&labelColor=&style=for-the-badge" height="30" alt="instagram logo"  />
  </a>
  <a href="https://t.me/BlackGoku_69th" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Telegram&logo=telegram&label=&color=2CA5E0&logoColor=white&labelColor=&style=for-the-badge" height="30" alt="telegram logo"  />
  </a>
  <a href="https://discord.com/users/571299781096505344" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Discord&logo=discord&label=&color=7289DA&logoColor=white&labelColor=&style=for-the-badge" height="30" alt="discord logo"  />
  </a>
</div>
