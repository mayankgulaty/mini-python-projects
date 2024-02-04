import json
import os

def load_vocabulary(filename='vocabulary.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return {}

def save_vocabulary(vocabulary, filename='vocabulary.json'):
    with open(filename, 'w') as file:
        json.dump(vocabulary, file, indent=4)

def add_word(vocabulary):
    word = input("Enter the new word: ")
    meaning = input("Enter the meaning of the word: ")
    example = input("Enter an example sentence: ")

    vocabulary[word] = {'meaning': meaning, 'example': example}
    save_vocabulary(vocabulary)
    print(f"'{word}' added to your vocabulary.")

def review_vocabulary(vocabulary):
    if not vocabulary:
        print("Your vocabulary list is empty.")
        return
    for word, data in vocabulary.items():
        print(f"\nWord: {word}\nMeaning: {data['meaning']}\nExample: {data['example']}")

def search_word(vocabulary):
    word = input("Enter the word to search: ")
    if word in vocabulary:
        data = vocabulary[word]
        print(f"\nWord: {word}\nMeaning: {data['meaning']}\nExample: {data['example']}")
    else:
        print("Word not found in your vocabulary.")

def main():
    vocabulary = load_vocabulary()

    while True:
        action = input("\nChoose an action - Add Word (A), Review (R), Search (S), Exit (E): ").upper()

        if action == 'A':
            add_word(vocabulary)

        elif action == 'R':
            review_vocabulary(vocabulary)

        elif action == 'S':
            search_word(vocabulary)

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
