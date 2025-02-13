# Here is a Python code for a basic AI voice assistant:

# Import necessary libraries
import speech_recognition as sr
import pyttsx3
import wikipedia
import datetime
import os

# Initialize the speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()

# Function which I have generated to  convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech and convert it to text
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            return query
        except Exception as e:
            print(e)
            speak("Sorry, I didn't catch that.")
            return None

# Function to wish the user based on the time of day
def wish_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning , I am ANIKET the A I assistant,,how may I help you!")
    elif hour < 18:
        speak("Good afternoon ,I am ANIKET the A I assistant,,how may I help you!")
    else:
        speak("Good evening,I am ANIKET the A I assistant,how may I help you!")

# Function to perform tasks based on user queries
def perform_tasks(query):
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = os.system("start https://www.wikipedia.com")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)
    elif 'time' in query:
        speak("The current time is ")
        speak(datetime.datetime.now().strftime("%H:%M:%S"))
    elif 'date' in query:
        speak("The current date is ")
        speak(datetime.datetime.now().strftime("%d-%m-%Y"))
    elif 'open google' in query:
        speak("Opening Google...")
        os.system("start https://www.google.com")
    elif 'exit' in query or 'quit' in query:
        speak("Goodbye!")
        exit()
    else:
        speak("I didn't understand that.")

# Main function
def main():
    wish_user()
    while True:
        query = recognize_speech().lower()
        if query is not None:
            perform_tasks(query)

if __name__ == "__main__":
    main()

# Here's a detailed explanation of the code:
#
# Importing Libraries
#
# The code starts by importing the necessary libraries:
#
# - speech_recognition for speech recognition
# - pyttsx3 for text-to-speech conversion
# - wikipedia for searching Wikipedia
# - datetime for getting the current time and date
# - os for opening Google
# #
# Initializing Speech Recognition and Text-to-Speech Engines
#
# The code initializes the speech recognition and text-to-speech engines:
#
# - r = sr.Recognizer() initializes the speech recognition engine
# - engine = pyttsx3.init() initializes the text-to-speech engine
#
# Functions
#
# The code defines several functions:
#
# - speak(text): converts text to speech using the pyttsx3 library
# - recognize_speech(): recognizes speech and converts it to text using the speech_recognition library
# - wish_user(): wishes the user based on the time of day
# - perform_tasks(query): performs tasks based on user queries
#
# Main Function
#
# The main() function is the entry point of the program. It:
#
# - Calls the wish_user() function to wish the user
# - Enters an infinite loop where it:
#     - Calls the recognize_speech() function to recognize speech
#     - Calls the perform_tasks(query) function to perform tasks based on user queries
#
# Performing Tasks
#
# The perform_tasks(query) function performs tasks based on user queries. It checks for specific keywords in the query and performs the corresponding task. For example:
#
# - If the query contains the keyword "wikipedia", it searches Wikipedia and reads out the results.
# - If the query contains the keyword "time", it tells the current time.
# - If the query contains the keyword "date", it tells the current date.
# - If the query contains the keyword "open google", it opens Google in the default web browser.
# - If the query contains the keyword "exit" or "quit", it exits the program.

