import requests

def send_request(prompt):
    data = {
        "input": {
            "input": prompt
        }
    }
    headers = {"Authorization": "Basic <API Key>"}
    response = requests.post(
        "<Endpoint URL>",
        json=data,
        headers=headers
    )
    return response.json()

def chatbot_interface():
    print("Welcome to the Prompt Machine! Type 'quit' to exit.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "quit":
            break

        # Send user input to the Spellbook API
        response = send_request(user_input)

        # Extract the response and print it
        bot_response = response['output']
        print("Bot:", bot_response)

if __name__ == "__main__":
    chatbot_interface()