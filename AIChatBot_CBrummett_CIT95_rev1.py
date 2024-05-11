import streamlit as st  # Import the Streamlit library for building the user interface
import openai  # Import the OpenAI library for interacting with the OpenAI API
from dotenv import load_dotenv  # Import the dotenv library for loading environment variables from a .env file
import os  # Import the os library for interacting with the operating system
from openai import OpenAI
# Load environment variables from .env file
load_dotenv() 

# Retrieve the API key from environment variables
api_key = os.getenv('OPENAI_API_KEY')

# Configure the OpenAI library with your API key
openai.api_key = api_key

# Initialize Streamlit application
st.title("Python Programming Assistant")  # Set the title of the Streamlit app
user_input = st.text_input("Ask me anything about Python programming:", "")  # Create a text input field for the user to enter their question
st.write("Your question:", user_input)  # Display the user's question on the screen

client = OpenAI()  # Create an instance of the OpenAI client

if user_input:  # Check if the user has entered a question
    completion = client.chat.completions.create(  # Call the OpenAI API to generate a response to the user's question
        model="gpt-3.5-turbo",  # Set the model to use for generating the response
        messages=[
            {"role": "user", "content": user_input},  # Set the user's question as the content of the message
        ]
    )
    answer = completion.choices[0].message.content
    st.write(answer)  # Display the generated response on the screen
