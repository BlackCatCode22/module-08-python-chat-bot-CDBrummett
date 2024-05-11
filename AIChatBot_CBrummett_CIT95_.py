import streamlit as st  # Import the Streamlit library for building the user interface
import openai  # Import the OpenAI library for interacting with the OpenAI API
from dotenv import load_dotenv  # Import the dotenv library for loading environment variables from a .env file
import os  # Import the os library for interacting with the operating system

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from environment variables
api_key = os.getenv('OPENAI_API_KEY')

# Configure the OpenAI library with your API key
openai.api_key = api_key

# Initialize Streamlit application
st.title("Python Programming Assistant")  # Set the title of the Streamlit app

# Initialize chat memory
chat_memory = []

# Create a text input field for the user to enter their question
user_input = st.text_input("Ask me anything about Python programming:", "")

# Display the user's question on the screen
st.write("Your question:", user_input)

# Create an instance of the OpenAI client
client = OpenAI()

# Check if the user has entered a question
if user_input:
    # Add the user's question to the chat memory
    chat_memory.append({"role": "user", "content": user_input})

    # Call the OpenAI API to generate a response to the user's question
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Set the model to use for generating the response
        messages=chat_memory  # Use the chat memory as the context for the response
    )

    # Add the assistant's response to the chat memory
    chat_memory.append({"role": "assistant", "content": completion.choices[0].message.content})

    # Display the generated response on the screen
    st.write(completion.choices[0].message.content)
