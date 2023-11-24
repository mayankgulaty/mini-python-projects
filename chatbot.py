import random


class Chatbot:
    def __init__(self):
        self.memory = {}

    def get_response(self, user_input):
        greetings = ["Hello!", "Hi there!", "Hey!", "Greetings!"]
        farewells = ["Goodbye!", "Farewell!", "Bye!", "See you!"]
        compliments = ["You're awesome!", "Great job!", "Well done!", "You rock!"]
        gratitude_responses = ["You're welcome!", "No problem!", "Anytime!"]

        if "hello" in user_input.lower():
            return random.choice(greetings)
        elif "bye" in user_input.lower():
            return random.choice(farewells)
        elif "thank you" in user_input.lower():
            return random.choice(gratitude_responses)
        elif "how are you" in user_input.lower():
            return "I'm just a computer program, but thanks for asking!"
        elif "your name" in user_input.lower():
            return "I'm Chatbot. Nice to meet you!"
        elif "my name is" in user_input.lower():
            user_name = user_input.split("is", 1)[1].strip()
            self.memory['user_name'] = user_name
            return f"Nice to meet you, {user_name}!"
        elif "favorite color" in user_input.lower():
            return self.get_favorite_color_response()
        else:
            return random.choice(compliments)

    def get_favorite_color_response(self):
        if 'user_name' in self.memory:
            return f"{self.memory['user_name']}, what's your favorite color?"
        else:
            return "What's your favorite color?"


def chat():
    chatbot = Chatbot()
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break

        response = chatbot.get_response(user_input)
        print("Chatbot:", response)


if __name__ == "__main__":
    chat()
