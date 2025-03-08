from chatbot import input_command, say
from open_app import open_app


def main():
    say("Hello! How can I assist you?")

    while True:
        command = input_command().lower()

        if "exit" in command or "stop" in command:
            say("Goodbye! Have a great day.")
            break

        elif "open app" in command:
            say("Which application would you like to open?")
            app_name = input_command().lower().strip()

            if app_name in ["none", ""]:
                say("No application name provided.")
            else:
                open_app(app_name)
                say(f"Opening {app_name}.")

        elif command != "none":
            say(f"You said: {command}")


if __name__ == "__main__":
    main()
