from openai import OpenAI

OPENAI_API_KEY = ""
client = OpenAI(api_key = OPENAI_API_KEY)

messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant"
    }
]

while True:
    message = input("You: ")
    messages.append(
        {
            "role": "user",
            "content": message
        },
    )
    chat = client.chat.completions.create(
        messages=messages,
        model="whisper-1"
    )

    reply = chat.choices[0].message

    print("Assistant: ", reply.content)
    
    messages.append(reply)