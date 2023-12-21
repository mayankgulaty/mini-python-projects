import random

def get_daily_quote():
    quotes = [
        "Believe you can and you're halfway there. – Theodore Roosevelt",
        "The only way to do great work is to love what you do. – Steve Jobs",
        "The best time to plant a tree was 20 years ago. The second best time is now. – Chinese Proverb",
        # Add more quotes as desired
    ]
    return random.choice(quotes)

def main():
    quote_of_the_day = get_daily_quote()
    print("Today's Motivational Quote:")
    print(quote_of_the_day)

if __name__ == "__main__":
    main()
