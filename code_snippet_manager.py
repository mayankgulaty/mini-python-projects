import json
import os

def save_snippets(snippets):
    with open('snippets.json', 'w') as file:
        json.dump(snippets, file, indent=4)

def load_snippets():
    if not os.path.exists('snippets.json'):
        return {}
    with open('snippets.json', 'r') as file:
        return json.load(file)

def add_snippet(snippets, title, category, code):
    snippets[title] = {'category': category, 'code': code}
    save_snippets(snippets)
    print("Snippet added successfully.")

def view_snippets(snippets):
    for title, data in snippets.items():
        print(f"\nTitle: {title}\nCategory: {data['category']}\nCode: {data['code']}")

def main():
    snippets = load_snippets()

    while True:
        action = input("\nChoose an action - Add (A), View (V), Exit (E): ").upper()

        if action == 'A':
            title = input("Enter the snippet title: ")
            category = input("Enter the snippet category: ")
            code = input("Enter the snippet code: ")
            add_snippet(snippets, title, category, code)

        elif action == 'V':
            view_snippets(snippets)

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
