# Telegram Chat Fetcher

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

## Installation

1. Clone this repository
2. Create a virtual environment and activate it:

```sh
    python -m venv .venv
    source .venv/bin/activate  # On macOS/Linux
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

> Replace `your_api_id` and `your_api_hash` with your Telegram API credentials.

___
## Usage

1. Run the script

```sh
    python retrieve_messages.py
```

2. Sign in using your phone number (OTP-based authentication).

3. The script will list all available chats. Enter the chat name or ID to fetch messages.

4. Messages will be saved in a JSON file in the format: chat_<chat_id>.json.
