from chatbot import input_command, say
from open_app import open_app
import pymongo
from datetime import datetime

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["course_db"]
chats_collection = db["chats"]


def store_chat(user_message, bot_response):
    chat_entry = {
        "user_message": user_message,
        "bot_response": bot_response,
        "timestamp": datetime.now()
    }
    chats_collection.insert_one(chat_entry)


def main():
    say("Hello! How can I assist you?")
    print("Bot: Hello! How can I assist you? ")

    while True:
        command = input_command()
        print(f"User: {command}")

        if "exit" in command or "stop" in command:
            bot_response = "Goodbye! Have a great day."
            say(bot_response)
            print(f"Bot: {bot_response}")
            store_chat(command, bot_response)
            break

        elif "open app" in command:
            say("Which application would you like to open?")
            print("Bot: Which application would you like to open? ")

            app_name = input_command()

            while not app_name:
                print("Bot: I didn't catch that. Please type the application name.")
                app_name = input_command()

            print(f"User: {app_name}")

            open_app(app_name)
            bot_response = f"Opening {app_name}."
            say(bot_response)
            print(f"Bot: {bot_response}")
            store_chat(command, bot_response)

        else:
            bot_response = f"You said: {command}"
            say(bot_response)
            print(f"Bot: {bot_response}")
            store_chat(command, bot_response)


if __name__ == "__main__":
    main()
