import openai
import json
from dotenv import dotenv_values

config = dotenv_values(".env")

openai.api_key  = config["OPENAI_API_KEY"]

messages = []
messages.append(
    {
        "role": "system",
        "content": "You're my bot assistant."
    }
)

def ask_chatgpt():
  completion = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=messages,
          max_tokens=200,
          top_p=0.5,
          frequency_penalty=0,
          presence_penalty=0
      )
  messages.append(completion["choices"][0]["message"].to_dict())
  print(f"ChatBot: {completion.choices[0].message.content}")


while True:
  try:
    user_input = input("You: ")
    messages.append(
        {
            "role": "user",
            "content": f"{user_input}"
        }
    )
    ask_chatgpt()
  except KeyboardInterrupt:
    print("Exiting...")
    messages = []
    break