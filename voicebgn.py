import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio)
            return query.lower()
        except:
            speak("Sorry, I didn't catch that.")
            return ""

def respond(query):
    if "hello" in query:
        speak("Hello there!")
    elif "time" in query:
        time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {time}")
    elif "date" in query:
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {date}")
    elif "search" in query:
        search_term = query.replace("search", "")
        speak(f"Searching for {search_term}")
        webbrowser.open(f"https://www.google.com/search?q={search_term}")
    else:
        speak("I don't understand that command yet.")

while True:
    query = listen()
    respond(query)
