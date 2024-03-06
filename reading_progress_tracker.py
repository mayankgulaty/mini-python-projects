import json
import os

def load_reading_list(filename='reading_list.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return {'Want to Read': [], 'Currently Reading': [], 'Read': []}

def save_reading_list(reading_list, filename='reading_list.json'):
    with open(filename, 'w') as file:
        json.dump(reading_list, file, indent=4)

def add_book(reading_list):
    title = input("Enter the book title: ")
    category = input("Enter the category (Want to Read, Currently Reading, Read): ")
    if category in reading_list:
        reading_list[category].append(title)
        save_reading_list(reading_list)
        print(f"'{title}' added to '{category}'.")
    else:
        print("Invalid category.")

def update_book_status(reading_list):
    title = input("Enter the book title to update: ")
    new_category = input("Enter the new category for the book (Want to Read, Currently Reading, Read): ")
    for category in reading_list:
        if title in reading_list[category]:
            reading_list[category].remove(title)
            reading_list[new_category].append(title)
            save_reading_list(reading_list)
            print(f"'{title}' moved to '{new_category}'.")
            return
    print("Book not found.")

def view_reading_list(reading_list):
    for category, books in reading_list.items():
        print(f"\n{category}:")
        for book in books:
            print(f"- {book}")

def main():
    reading_list = load_reading_list()

    while True:
        action = input("\nChoose an action - Add Book (A), Update Status (U), View List (V), Exit (E): ").upper()

        if action == 'A':
            add_book(reading_list)

        elif action == 'U':
            update_book_status(reading_list)

        elif action == 'V':
            view_reading_list(reading_list)

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
