import pyaudio
import pyttsx3
import speech_recognition as sr
import keyboard

voice_mode = True


def toggle_input_mode():
    global voice_mode
    voice_mode = not voice_mode
    mode = "Voice Input Enabled" if voice_mode else "Text Input Enabled"
    print(f"Mode Switched: {mode}")
    say(mode) if voice_mode else None


def input_command():
    global voice_mode
    if voice_mode:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 1
            print("Listening... (Press 'Shift' to switch mode)")

            try:
                audio = r.listen(source, timeout=5)
                print("Interpreting....")
                query = r.recognize_google(audio, language="en-in")
                print(f"User said: {query}")
                return query

            except sr.UnknownValueError:
                say("I did not get that. Can you say it again?")
                return "none"

            except sr.RequestError:
                say("I am having trouble connecting to the service.")
                return "none"

            except sr.WaitTimeoutError:
                print("No voice detected.")
                return "none"
    else:
        return get_text_input()


def get_text_input():
    return input("Type your command: ")


def say(text):
    global voice_mode
    if voice_mode:
        print(f"Speaking: {text}")
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    else:
        print(f"Bot: {text}")


keyboard.add_hotkey("shift", toggle_input_mode)