import openai
import os


def generate_response(user_input, api_key):
    try:
        # Call the OpenAI API to generate a response
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system",
                       "content": "Assume the role of a Python teacher, and think step by step. Your name is Skippy Py."},
                      {"role": "user", "content": user_input}]
        )

        # Extract the text of the response
        response_text = completion['choices'][0]['message']['content']
        return response_text
    except openai.error.APIError as e:
        # Print an error message if the API call fails
        print("Error generating response:", e)
        return "I'm sorry, I couldn't generate a response."


def print_welcome_message():
    print("\nWelcome to the Python Study Bot! Type 'quit' to exit.\n")


def run_chatbot(api_key):
    print_welcome_message()

    while True:
        user_input = input("Python student question: ")

        if user_input.lower() == "quit":
            print("Exiting Python Study Bot.")
            break

        response = generate_response(user_input, api_key)
        print("Python Study Bot:", response)


def main():
    api_key = os.environ.get("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")
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable is not set.")
        return

    run_chatbot(api_key)


if __name__ == "__main__":
    main()
