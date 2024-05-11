# pip install python-dontenv openai
# pip install --upgrade openai
# pip install --upgrade pythondotenv
import openai


class Chatbot:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.memory = []

    def generate_response(self, user_input: str) -> str:
        try:
            # Create a new message with the user's input
            new_message = {"role": "user", "content": user_input}

            # Add the new message to the conversation memory
            self.memory.append(new_message)

            # Create a system message to provide context for the model
            system_message = {"role": "system", "content": "Assume the role of a Python teacher, and think step by step. Your name is Skippy Py."}

            # Create a list of messages to send to the model
            messages = [system_message] + self.memory

            # Call the OpenAI API to generate a response
            completion = client.chat.completions.create.create(
                model="gpt-3.5-turbo",
                api_key=self.api_key,
                messages=messages
            )

            # Extract the text of the response
            response_text = completion.choices[0].message.content

            # Add the response to the conversation memory
            self.memory.append({"role": "assistant", "content": response_text})

            return response_text
        except openai.OpenAIError as e:
            raise Exception("Error generating response:", e)

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
            except Exception as e:
                print("Error:", e)


def main() -> None:
    try:
        api_key = "OPENAI_API_KEY"
        chatbot = Chatbot(api_key)
        chatbot.run_chatbot()
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
