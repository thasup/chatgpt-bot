import openai
import json
from dotenv import dotenv_values

config = dotenv_values(".env")

openai.api_key  = config["OPENAI_API_KEY"]

def get_and_render_prompt_chat(text):
    messages = [
        {
            "role": "system",
            "content": "You're my bot assistant."
        },
        {
            "role": "user",
            "content": f"{text}"
        },
    ]

    completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=200,
            top_p=0.5,
            frequency_penalty=0,
            presence_penalty=0
        )
    print(completion.choices[0].message.content)
    print("-----")
    print(completion)

get_and_render_prompt_chat("Tell a short inspiration story.")