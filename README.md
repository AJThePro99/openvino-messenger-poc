# Telegram Chat Fetcher

> This is phase one of the proof of concept for [OpenVINO Messenger AI-Assistant for AI PC](https://github.com/openvinotoolkit/openvino/wiki/Google-Summer-Of-Code#2-openvino-messenger-ai-assistant-for-an-ai-pc)
>
> Currently, the PoC can connect to a user's telegram account and fetch their chat history and store it a `.json` file

## For a direct view of outputs, check out [PoC Example Pictures | PICTURES.md](https://github.com/AJThePro99/openvino-messenger-poc/blob/main/pictures-proof/PICTURES.md)

This script retrieves messages from a user's Telegram chats using the **Telethon** library.

## Features

- Fetches a list of all available chats
- Allows the user to select a chat by name or ID
- Retrieves and saves the last 10 messages from the selected chat
- Saves messages in a JSON file for later use

## Prerequisites

Ensure you have:

- A Telegram account
- API credentials (API ID and API HASH) from [my.telegram.org](https://my.telegram.org)

### Steps to get `API_ID` and `API_HASH`

- Go to [my.telegram.org](https://my.telegram.org)
- Log in with your phone number
- Select API development tools
- Fill in the form to create your app
- Copy the `App api_id` and paste it into `.env` as `API_ID`
- Copy the `App api_hash` and paste it into `.env` as `API_HASH`

## Installation

1. Clone this repository
2. Create a virtual environment and activate it:

    ```sh
        python -m venv .venv
    ```

    ```sh
        source .venv/bin/activate  # On macOS/Linux
    ```

    ```sh
        .venv\Scripts\activate     # On Windows
    ```

3. Install dependencies

    ```sh
        pip install -r requirements.txt
    ```

4. Create a `.env` file in the **project root** and add the following:

    ```sh
        API_ID=your_api_id
        API_HASH=your_api_hash
    ```

    > Replace `your_api_id` and `your_api_hash` with your Telegram API credentials if not done so already.

## Usage

1. Run the script

    ```sh
        python retrieve_messages.py
    ```

2. Sign in using your phone number (OTP-based authentication).
    > Phone number in the format of `+CCXXXXXXXXXX` country code, followed by your phone number
3. The script will list all available chats. Enter the chat name or ID to fetch messages.
4. Messages will be saved in a JSON file in the format: `chat_<chat_id>`.json.

___

# What this proves

> Have a look at [PICTURES.md](https://github.com/AJThePro99/openvino-messenger-poc/blob/main/pictures-proof/PICTURES.md) so that you fully understand what this program does

For this [particular project](https://github.com/openvinotoolkit/openvino/wiki/Google-Summer-Of-Code#2-openvino-messenger-ai-assistant-for-an-ai-pc),
there are four main parts:

1.Fetching chat history from Telegram using the API

    - This prototype successfully retrieves chat messages from a Telegram account, demonstrating that we can access user conversations and store them locally.

    - This lays the foundation for message retrieval, ensuring that relevant conversation data is accessible for further processing.

2.Storing messages for further processing

    - The prototype stores chat messages in JSON format, allowing structured storage for later retrieval.

    - This proves that we can persist conversation data, which will be crucial for later stages like embedding generation and retrieval-augmented generation (RAG).

3.Preprocessing messages for semantic search and retrieval

    - (Upcoming) The next phase will involve converting these raw messages into a format suitable for semantic retrieval (e.g., embeddings stored in a vector database).

    - This will allow for searching and retrieving relevant messages when answering user queries.

4.Integration with an AI model to enhance interaction

    - (Upcoming) Eventually, this stored and preprocessed data will be used to provide context to an LLM running on OpenVINO, enabling intelligent responses and summarization.

    - This proof of concept ensures that a reliable pipeline for retrieving user messages is established, which is a critical step toward building an interactive AI assistant.


## This prototype proves that

We can authenticate users via Telegram’s API and retrieve messages programmatically.
We can store and structure this data for further processing.
We have a working base that can be expanded to support semantic search, vector storage, and AI-assisted responses.

With this foundation in place, the next steps will focus on vectorizing the messages, storing them efficiently, and implementing retrieval techniques to make the AI assistant more effective.

---

Ideas and opinions are welcome!
Just open a PR :)
