import os
import openai
#importing dotenv to access the environment variable open ai key #from .env file
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

#using the while loop to continously take inputs from user and
#give responses like in a chat
while True:
    user_input = input("You: ")  # Get user input

    # Create a list of messages with the user's input
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_input}
    ]

    # Make the API call
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    # Print the assistant's response
    print("Assistant:", completion.choices[0].message["content"])

    # Ask whether to continue or stop
    user_choice = input("Continue? (y/n): ")
    if user_choice.lower() != "y":
        print("Glad to help bye!")
        break  # Exit the loop if the user doesn't want to continue