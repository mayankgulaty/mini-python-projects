import random

# Function to get a response from the chatbot
def get_response(user_input):
    greetings = ["Hello!", "Hi there!", "Hey!", "Greetings!"]
    farewells = ["Goodbye!", "Farewell!", "Bye!", "See you!"]
    compliments = ["You're awesome!", "Great job!", "Well done!", "You rock!"]
    responses = [greetings, farewells, compliments]

    if "hello" in user_input.lower():
        return random.choice(greetings)
    elif "bye" in user_input.lower():
        return random.choice(farewells)
    elif "thank you" in user_input.lower():
        return "You're welcome!"
    elif "how are you" in user_input.lower():
        return "I'm just a computer program, but thanks for asking!"
    else:
        return random.choice(random.choice(responses))

# Main function for the chat
def chat():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print("Chatbot:", response)

# Run the chat program
if __name__ == "__main__":
    chat()
