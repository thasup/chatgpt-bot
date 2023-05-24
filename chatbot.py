import openai
import argparse
from dotenv import dotenv_values

config = dotenv_values(".env")

openai.api_key  = config["OPENAI_API_KEY"]

def main():
  parser = argparse.ArgumentParser(description="Simple command line chatbot with GPT-3.5")
  parser.add_argument(
    "--personality",
    type=str,
    help="A brief summary of the chatbot's personality",
    default="friendly and helpful chatbot"
  )
  args = parser.parse_args()

  messages = []
  messages.append(
      {
          "role": "system",
          "content": f"You're a conversational chatbot. Your personality is : {args.personality}"
      }
  )

  def ask_chatgpt():
    completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=200,
            top_p=0.5,
            frequency_penalty=0,
            presence_penalty=0,
            stream=True
        )
    messages.append(completion["choices"][0]["message"].to_dict())

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

if __name__ == "__main__":
  main()