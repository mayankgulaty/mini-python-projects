import random
import nltk
import wikipediaapi
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from newsapi import NewsApiClient

nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")


class Chatbot:
    def __init__(self):
        self.memory = {}
        self.stop_words = set(stopwords.words("english"))
        self.lemmatizer = WordNetLemmatizer()
        self.wiki_wiki = wikipediaapi.Wikipedia("en", headers={"User-Agent": "Chatbot/1.0 (YourContactInformation)"})
        self.newsapi = NewsApiClient(api_key="YOUR_NEWS_API_KEY")  # Replace with your News API key

    def preprocess_input(self, user_input):
        tokens = word_tokenize(user_input.lower())
        filtered_tokens = [self.lemmatizer.lemmatize(token) for token in tokens if
                           token.isalnum() and token not in self.stop_words]
        return " ".join(filtered_tokens)

    def get_response(self, user_input):
        user_input = self.preprocess_input(user_input)

        greetings = ["Hello!", "Hi there!", "Hey!", "Greetings!"]
        farewells = ["Goodbye!", "Farewell!", "Bye!", "See you!"]
        compliments = ["You're awesome!", "Great job!", "Well done!", "You rock!"]
        gratitude_responses = ["You're welcome!", "No problem!", "Anytime!"]

        if "hello" in user_input:
            return random.choice(greetings)
        elif "bye" in user_input:
            return random.choice(farewells)
        elif "thank you" in user_input:
            return random.choice(gratitude_responses)
        elif "how are you" in user_input:
            return "I'm just a computer program, but thanks for asking!"
        elif "your name" in user_input:
            return "I'm Chatbot. Nice to meet you!"
        elif "my name is" in user_input:
            user_name = user_input.split("is", 1)[1].strip()
            self.memory['user_name'] = user_name
            return f"Nice to meet you, {user_name}!"
        elif "favorite color" in user_input:
            return self.get_favorite_color_response()
        elif "joke" in user_input:
            return self.get_joke_response()
        elif "weather" in user_input:
            return self.get_weather_response()
        elif "tell me about" in user_input:
            return self.get_wikipedia_response(user_input)
        elif "recommend a book" in user_input:
            return self.get_book_recommendation()
        elif "news" in user_input:
            return self.get_news_headlines()
        elif "recommend a movie" in user_input:
            return self.get_movie_recommendation()
        elif "what is" in user_input or "who is" in user_input:
            return self.get_general_knowledge_response(user_input)
        else:
            return random.choice(compliments)

    def get_favorite_color_response(self):
        if 'user_name' in self.memory:
            return f"{self.memory['user_name']}, what's your favorite color?"
        else:
            return "What's your favorite color?"

    def get_joke_response(self):
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Parallel lines have so much in common. It's a shame they'll never meet.",
            "I told my wife she was drawing her eyebrows too high. She looked surprised.",
            "Why did the scarecrow win an award? Because he was outstanding in his field!"
        ]
        return random.choice(jokes)

    def get_weather_response(self):
        # Provide a basic weather response (simulated)
        return "The weather is great today!"

    def get_wikipedia_response(self, user_input):
        # Extract the topic from the user's input
        topic = user_input.split("about", 1)[1].strip()

        # Retrieve information from Wikipedia
        page_py = self.wiki_wiki.page(topic)
        if page_py.exists():
            return f"Here's some information about {topic}: {page_py.text[:200]}..."
        else:
            return f"Sorry, I couldn't find information about {topic} on Wikipedia."

    def get_book_recommendation(self):
        # Suggest a random book (simulated)
        books = [
            "The Great Gatsby by F. Scott Fitzgerald",
            "To Kill a Mockingbird by Harper Lee",
            "1984 by George Orwell",
            "The Catcher in the Rye by J.D. Salinger",
            "Pride and Prejudice by Jane Austen"
        ]
        return f"I recommend you check out: {random.choice(books)}"

    def get_news_headlines(self):
        # Retrieve the latest news headlines
        news_headlines = self.newsapi.get_top_headlines(country="us", language="en")
        if "articles" in news_headlines and len(news_headlines["articles"]) > 0:
            headlines = [article["title"] for article in news_headlines["articles"][:5]]
            return "Here are some top headlines:\n" + "\n".join(headlines)
        else:
            return "Sorry, I couldn't retrieve the latest news headlines."

    def get_movie_recommendation(self):
        # Suggest a random movie (simulated)
        movies = [
            "The Shawshank Redemption",
            "The Godfather",
            "Pulp Fiction",
            "The Dark Knight",
            "Schindler's List"
        ]
        return f"I recommend you watch: {random.choice(movies)}"

    def get_general_knowledge_response(self, user_input):
        # Extract the topic from the user's input
        topic = user_input.split("is", 1)[1].strip()

        # Retrieve a summary from Wikipedia
        page_py = self.wiki_wiki.page(topic)
        if page_py.exists():
            return f"Here's a summary about {topic}: {page_py.text[:200]}..."
        else:
            return f"Sorry, I couldn't find information about {topic} on Wikipedia."


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
