from telethon.sync import TelegramClient
import os
import json
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")

# Ensure credentials are loaded
if not API_ID or not API_HASH:
    raise ValueError("Missing API_ID or API_HASH. Check your .env file.")

API_ID = int(API_ID)

# Start Telegram Client
client = TelegramClient("user_session", API_ID, API_HASH)

async def fetch_chats():
    """ Fetch and display user chats. """
    print("\nFetching your chats...\n")
    chats = []
    
    async for dialog in client.iter_dialogs():
        print(f"Chat Name: {dialog.name}, ID: {dialog.id}")
        chats.append({"name": dialog.name, "id": dialog.id})

    return chats

async def fetch_messages(chat_id):
    """ Fetch messages from a given chat. """
    print(f"\nFetching messages from chat ID {chat_id}...\n")
    messages = []

    async for message in client.iter_messages(chat_id, limit=10):  # Fetch last 10 messages
        sender = message.sender_id or "Unknown"
        messages.append({"sender": sender, "text": message.text, "date": str(message.date)})

    return messages

async def main():
    """ Main function to interact with Telegram API. """
    await client.start()
    print("Signed in successfully!")

    chats = await fetch_chats()
    
    # Let user select a chat by name
    chat_name = input("\nEnter chat name (or chat ID) to fetch messages: ").strip()

    # Find chat ID if user entered a name
    chat_id = None
    for chat in chats:
        if chat["name"].lower() == chat_name.lower() or str(chat["id"]) == chat_name:
            chat_id = chat["id"]
            break

    if not chat_id:
        print("Chat not found! Exiting.")
        return

    messages = await fetch_messages(chat_id)
    
    # Save messages to JSON
    filename = f"chat_{chat_id}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(messages, f, indent=4)

    print(f"\nMessages saved to {filename}")

# Run the client
with client:
    client.loop.run_until_complete(main())
