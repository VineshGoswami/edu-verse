import pyaudio
import pyttsx3
import speech_recognition as sr


def input_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        print("Listening...")
        audio = r.listen(source)

        try:
            print("Interpreting....")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query

        except sr.UnknownValueError:
            say("I did not get that. Can you say it again?")
            return "none"

        except sr.RequestError:
            say("I am having trouble connecting to the speech recognition service.")
            return "none"


def say(text):
    print(f"Speaking: {text}")
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()



