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
    print("Welcome to the Chatbot! Type 'quit' to exit.")
    context = []

    while True:
        user_input = input("You: ")

        if user_input.lower() == "quit":
            break

        # Add user input to the context
        context.append("You: " + user_input)

        # Send context to the Spellbook API
        response = send_request(" ".join(context))

        # Extract the response and print it
        bot_response = response['output']
        print("Bot:", bot_response)

        # Add bot response to the context
        context.append("Bot: " + bot_response)

if __name__ == "__main__":
    chatbot_interface()