import speech_recognition as sr
import pyttsx3
from transformers import pipeline

# Initialize speech recognition
recognizer = sr.Recognizer()

# Initialize text-to-speech
engine = pyttsx3.init()

# Initialize natural language understanding pipeline
nlu_pipeline = pipeline("ner", model="KB/bert-base-swedish-cased-ner")

# Function to recognize speech
def recognize_speech():
    with sr.Microphone(device_index = 4) as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        # Use Google Web Speech API for speech recognition
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand what you said."
    except sr.RequestError as e:
        return "Sorry, could not request results from Google Speech Recognition service; {0}".format(e)

# Function to perform natural language understanding
def understand_text(text):
    entities = nlu_pipeline(text)
    return entities

# Function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Main loop
while True:
    command = recognize_speech().lower()
    print("You said:", command)
    entities = understand_text(command)
    # Process entities and perform actions based on user command
    # You can use the entities to understand user intents and extract relevant information
