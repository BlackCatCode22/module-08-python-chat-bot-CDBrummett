# Import necessary libraries
import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key from environment variable
openai.api_key = os.getenv("openaiAPI")

# Function to create a chat completion using the OpenAI API
def create_chat_completion(model, messages):
    # Call the OpenAI API to generate a response
    completions = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )
    # Return the generated response
    return completions.choices[0].message

# Set the model to use for generating responses
model = "gpt-3.5-turbo"

# Create a list of messages to send to the model
messages = [
    # Create a system message to provide context for the model
    {"role": "system", "content": "You are a wonderful assistant and you explain all things python completely."},
    # Create a user message with a question for the model
    {"role": "user", "content": "Teach me about lists in python and write sample code."}
]

# Call the create_chat_completion function to generate a response
response = create_chat_completion(model, messages)

# Print the generated response
print(response)
