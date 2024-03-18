import speech_recognition as sr
import pyttsx3
from openai import OpenAI

OPENAI_API_KEY = ""
client = OpenAI(api_key = OPENAI_API_KEY)

# Initial message
messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant"
    }
]

# Initialize speech recognition
recognizer = sr.Recognizer()

# Initialize text-to-speech
engine = pyttsx3.init()

# To find the indices of all audio devices connected to the computer
# Use this to find out the device_index
#for index, name in enumerate(sr.Microphone().list_microphone_names()):
 #   print("Microphone {0}: {1}".format(index, name))

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

# Function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Main loop
while True:
    command = recognize_speech().lower()
    messages.append(
        {
            "role": "user",
            "content": command
        },
    )

    print("You said:", command)

    chat = client.chat.completions.create(
        messages=messages,
        model="whisper-1"
    )
    reply = chat.choices[0].message

    if "jarvis" in command:
        speak(reply.content)
        messages.append(reply)
