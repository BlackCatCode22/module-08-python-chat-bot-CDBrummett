import openai
import os

class APIError(Exception):
    pass

def generate_response(user_input: str, api_key: str) -> str:
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "Assume the role of a Python teacher, and think step by step. Your name is Skippy Py."},
                      {"role": "user", "content": user_input}]
        )
        return completion['choices'][0]['message']['content']
    except openai.error.APIError as e:
        raise APIError("Error generating response:", e)

def display_welcome_message() -> None:
    print("\nWelcome to the Python Study Bot! Type 'quit' to exit.\n")

def run_chatbot(api_key: str) -> None:
    display_welcome_message()
    while True:
        user_input = input("Python student question: ")
        if user_input.lower() == "quit":
            print("Exiting Python Study Bot.")
            break
        try:
            response = generate_response(user_input, api_key)
            print("Python Study Bot:", response)
        except APIError as e:
            print("Error:", e)

def load_api_key() -> str:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable is not set.")
    return api_key

def main() -> None:
    try:
        api_key = load_api_key()
        run_chatbot(api_key)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()