from chatbot import input_command, say
from open_app import open_app
from gemini import generate_text
import pymongo
from datetime import datetime

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["course_db"]
chats_collection = db["chats"]

text_input_mode = False


def store_chat(user_message, bot_response):
    chat_entry = {
        "user_message": user_message,
        "bot_response": bot_response,
        "timestamp": datetime.now()
    }
    chats_collection.insert_one(chat_entry)
    print(f"[Chat Stored] {chat_entry}")


def toggle_input_mode():
    global text_input_mode
    text_input_mode = not text_input_mode
    mode = "Text Input Enabled" if text_input_mode else "Voice Input Enabled"
    say(mode) if not text_input_mode else print(f"Mode Switched: {mode}")


def get_user_input():
    return input_command() if not text_input_mode else input("Type your command: ").strip()


def main():
    say("Hello! How can I assist you?")
    print("Bot: Hello! How can I assist you?")

    while True:
        command = get_user_input().lower()
        print(f"User: {command}")

        if "exit" in command or "stop" in command:
            bot_response = "Goodbye! Have a great day."
            say(bot_response)
            print(f"Bot: {bot_response}")
            store_chat(command, bot_response)
            break

        elif "open app" in command:
            say("Which application would you like to open?")
            print("Bot: Which application would you like to open?")
            app_name = get_user_input().lower().strip()
            if not app_name:
                app_name = input("Type application name: ").strip()

            open_app(app_name)
            bot_response = f"Opening {app_name}."
            say(bot_response)
            print(f"Bot: {bot_response}")
            store_chat(command, bot_response)

        elif "shift" in command:
            toggle_input_mode()

        else:
            bot_response = generate_text(command)
            if text_input_mode:
                print(f"Bot: {bot_response}")
            else:
                say(bot_response)
            store_chat(command, bot_response)


if __name__ == "__main__":
    main()
