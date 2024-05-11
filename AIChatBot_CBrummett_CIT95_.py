import os
import openai

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Set up system message
system_message = """You are a helpful assistant that provides detailed and helpful responses."""

# Set up user message
user_message = "What is the capital of France?"

# Set up chat completion
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message},
    ],
)

# Print assistant response
print(completion.choices[0].message.content)
