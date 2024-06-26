import streamlit as st
import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from environment variables
api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    # Raise an error if the API key is not set
    raise ValueError("OPENAI_API_KEY environment variable is not set")

# Configure the OpenAI library with your API key
openai.api_key = api_key

# Initialize Streamlit application
st.title("Python Programming Assistant")


def get_user_input(key):
    """
    Get user input from the text input field with a unique key
    """
    user_input = st.text_input("Ask me anything about Python programming:", key=key)
    st.write("Your question:", user_input)
    return user_input


def generate_response(user_input, conversation_history):
    """
    Generate a response to the user's input using the OpenAI API
    """
    try:
        # Create an instance of the OpenAI client
        client = openai.OpenAI()

        # Call the OpenAI API to generate a response to the user's question
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": user_input},
                *conversation_history
            ]
        )

        # Return the generated response
        return response.choices[0].message.content

    except openai.error.OpenAIError as e:
        # Return an error message if an OpenAI API error occurs
        return f"Error: {e}"


def main():
    """
    Main function to handle the conversation
    """
    conversation_history = []

    input_key1 = "input1"

    user_input1 = get_user_input(input_key1)

    while True:
        # Get user input
        user_input = user_input1

        if user_input:
            # Generate a response to the user's input
            response = generate_response(user_input, conversation_history)

            st.write(response)

            # Update the conversation history
            conversation_history.append({"role": "user", "content": user_input})
            conversation_history.append({"role": "assistant", "content": response})

            # Clear the input field
            user_input1 = ""
            ""


if __name__ == "__main__":
    # Run the main function
    main()
