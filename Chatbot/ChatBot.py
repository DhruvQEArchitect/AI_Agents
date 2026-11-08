from openai import OpenAI
from dotenv import load_dotenv
import os
from helper import Helper

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

models = client.models.list()

for model in models.data:
    print(model.id)

messages = [{"role": "system",
             "content": Helper.read_prompts("SeniorQA.md")}]

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = client.chat.completions.create(
        model=os.getenv("MODEL_PATH"),
        messages=messages
    )

    assistant_reply = response.choices[0].message.content

    messages.append({
        "role": "assistant",
        "content": assistant_reply
    })

    print("================Conversation History================")
    for message in messages:
        print(f'{message['role'].title()}: {message["content"]}')
    print(f"Bot: {assistant_reply}\n")
