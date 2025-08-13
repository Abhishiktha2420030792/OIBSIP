import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize recognizer & text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Text-to-speech function
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# Listen for voice input
def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand.")
        except sr.RequestError:
            speak("Network error.")
    return ""

# Main assistant logic
def run_assistant():
    speak("Hi, how can I help you?")
    command = listen()

    if "hello" in command:
        speak("Hello! How are you?")
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {current_time}")
    elif "date" in command:
        today = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today is {today}")
    elif "search" in command:
        speak("What should I search for?")
        query = listen()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak(f"Searching for {query}")
    else:
        speak("I can't do that yet.")

# Run the assistant
if __name__ == "__main__":
    run_assistant()
