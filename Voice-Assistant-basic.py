import speech_recognition as sr
import pyttsx3


recognizer = sr.Recognizer()
speaker = pyttsx3.init()
def listen_and_speak():
    try:
        with sr.Microphone() as source:
            print("Speak something...")
            audio = recognizer.listen(source)
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            speaker.say("You said: " + text)
            speaker.runAndWait()

    except sr.UnknownValueError:
        print("Sorry, could not understand your voice.")
        speaker.say("Sorry, I could not understand what you said.")
        speaker.runAndWait()
    except sr.RequestError:
        print("Could not request results from speech recognition service.")
        speaker.say("Sorry, there's an issue with the speech recognition service.")
        speaker.runAndWait()
listen_and_speak()
