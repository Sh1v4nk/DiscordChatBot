<div align="center">

# DiscordChatBot

[![code style: ruff](https://img.shields.io/badge/code_style-Ruff-orange?style=flat-square&logoColor=black)](https://github.com/astral-sh/ruff)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
![GitHub repo size](https://img.shields.io/github/repo-size/Sh1v4nk/DiscordChatBot)

Welcome to the repository for the **DiscordChatBot** project, a chatbot built using Python and powered by OpenAI's API to facilitate natural conversations on Discord. The bot leverages GPT-3.5 to create contextually fitting and human-like responses, making interactions with users more engaging and dynamic.

</div>

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Demo](#demo)
- [Technology Used](#technology-used)
- [Prerequisites & API Keys](#prerequisites--api-keys)
- [Installation](#installation)
- [Running the Bot](#running-the-bot)
- [Inviting the Bot to Your Server](#inviting-the-bot-to-your-server)
- [Usage](#usage)
- [Customization](#customization)
- [Further Exploration](#further-exploration)
- [Disclaimer](#disclaimer)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

The **DiscordChatBot** project demonstrates a Python-based Discord bot that interacts within a server, utilizing the OpenAI GPT-3.5 model for generating human-like responses. This bot is designed to maintain conversational context, ensuring dynamic and relevant interactions. By combining AI-driven responses with Discord's interactive platform, it opens up a world of engaging and lifelike conversations.

---

## Key Features

- **Discord Bot Integration**: The bot interacts within Discord servers, responding to mentions, facilitating conversations, and generating replies based on user input.
  
- **OpenAI GPT-3.5 Integration**: Leverages the powerful `text-davinci-003` model to generate coherent and contextually relevant responses, making interactions more natural.

- **Chat History Management**: The bot stores the last 10 messages in a conversation to maintain context and deliver better replies. This helps to generate more relevant and consistent responses in ongoing conversations.

- **Message Similarity Handling**: Uses Python’s `difflib` library to prevent repetition by comparing consecutive messages and ensuring a diverse range of responses.

- **Dynamic Prompt Generation**: Customizes prompts by including chat history and user input to maintain the flow of conversation. This ensures the bot generates responses that are coherent and contextually aware.

- **Token Management**: Limits responses to within OpenAI's token restriction (`max_tokens=256`) to ensure concise and meaningful interactions.

- **Asynchronous Processing**: Built using `Discord.py`, the bot can handle multiple messages asynchronously, ensuring a smooth experience even in larger servers.

---

## Demo

Here’s a quick look at the **DiscordChatBot** in action:

<div align="center">
<img width="auto" src="https://i.ibb.co/JHhbRqb/image.png" alt="DiscordChatBot Demo">
</div>

---

## Technology Used

- **[Python](https://www.python.org/):** Core language used to implement the bot and manage its functionalities.
  
- **[Discord.py](https://discordpy.readthedocs.io/en/stable/):** A Python library that interfaces with the Discord API, allowing for seamless bot integration.

- **[OpenAI API](https://openai.com/api/):** Provides access to OpenAI’s GPT-3.5 model for generating responses.

- **`difflib`**: A standard Python library that handles message similarity, ensuring the bot provides varied responses.

- **`.env` Files**: Used to store sensitive bot credentials securely.

---

## Prerequisites & API Keys

Before you begin, you'll need:

1. A **Discord bot token** from the [Discord Developer Portal](https://discord.com/developers/applications).
2. An **OpenAI API key** from the [OpenAI website](https://platform.openai.com/signup).

---

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

3. Create a new file in the root directory of the project and name it .env.

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

---

## Inviting the Bot to Your Server

1. Head over to the **Discord Developer Portal** and select your bot.
2. Navigate to the **OAuth2** section and generate an invite link by selecting the **bot** scope and choosing appropriate permissions (e.g., **Read Messages** and **Send Messages**).
3. Copy the generated OAuth2 URL, paste it into your browser, and select the server to invite the bot to.

---

## Usage

- **Mention the Bot**: To initiate a conversation, mention the bot in a message.
  
- **Auto-Response**: The bot will reply with a context-aware, AI-generated response based on the last 10 messages in the conversation.

---

## Customization

You can easily modify the bot's behavior by tweaking the settings in the `main.py` file:

- **OpenAI Model Parameters**: Adjust the model parameters (`temperature`, `max_tokens`, `top_p`, etc.) to control the bot's creativity and response length.

- **Message Similarity Threshold**: The `difflib.SequenceMatcher` ratio is set to `0.7` by default. Adjust this value to control how different the bot’s responses should be from previous ones.

- **Chat History Length**: The number of messages stored in chat history is controlled by the `MAX_CHAT_HISTORY` variable. Increase or decrease it to adjust the context size.

Refer to the [OpenAI API documentation](https://platform.openai.com/docs/api-reference/completions) for more insights on fine-tuning the GPT-3 model.

---

## Further Exploration

For advanced usage and ideas on how to extend the functionality of your bot:

- Experiment with different OpenAI prompts to shape the tone and style of the bot's responses.
- Add support for more commands, use cases, or even multi-language responses.

Check out the [OpenAI API documentation](https://platform.openai.com/docs/api-reference/introduction) for more ideas.

---

## Disclaimer

This bot is an example implementation using the OpenAI API, designed for educational purposes. The responses generated by the bot are influenced by the data used to train the model and may not always reflect accurate or appropriate information.

---

## Contributing

Contributions are welcome! 🎉 If you want to add features, fix bugs, or suggest improvements:

1. Fork the repository.
2. Create a new branch (`feature/your-feature-name`).
3. Submit a pull request when you're ready.

---

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Sh1v4nk/DiscordChatBot/blob/main/LICENSE) file for more details.

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
