from dotenv import load_dotenv
import os
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class Chatbot:
    def __init__(self):
        self.memory = []

    def generate_response(self, user_input: str) -> str:
        try:
            # Create a new message with the user's input
            new_message = {"role": "user", "content": user_input}

            # Add the new message to the conversation memory
            self.memory.append(new_message)

            # Create a system message to provide context for the model
            system_message = {"role": "system", "content": "You are a helpful assistant and you explain all things python completely."}

            # Create a list of messages to send to the model
            messages = [system_message] + self.memory

            # Call the OpenAI API to generate a response
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )

            # Extract the text of the response
            response_text = completion.choices[0].message.content

            # Add the response to the conversation memory
            self.memory.append({"role": "assistant", "content": response_text})

            return response_text
        except openai.OpenAIError as e:
            logging.error("Error generating response:", e)
            raise

    def run_chatbot(self) -> None:
        print("Welcome to the chatbot! Type 'quit' to exit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "quit":
                print("Exiting chatbot.")
                break
            try:
                response = self.generate_response(user_input)
                print("Assistant:", response)
            except openai.OpenAIError as e:
                logging.error("Error generating response:", e)
                print("Error:", e)

if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.run_chatbot()
