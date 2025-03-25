import os
from openai import OpenAI
from dotenv import load_dotenv

# load the secret stored in .env file
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    # Ensure the API key is available
    raise ValueError("Expected key to be set in the OPENAI_API_KEY environment variable")

# Create a chat client with the key
client = OpenAI(api_key=api_key)

def ask_chatgpt(user_message):
    # Use create function to generate a response.
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": 'you are a helpful assistant.'},
            {"role": "user", "content": user_message},
        ],
        temperature=0.7
    )
    # Return just the ocntent of the response.
    return response.choices[0].message.content
if __name__ == "__main__":
    # Executes the reqquest and returns the response
    response = ask_chatgpt("What is the capital of Nepal?")
    print(response) 

    # output: The capital of Nepal is Kathmandu.