import json
import os

def load_library(filename='library.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

def save_library(books, filename='library.json'):
    with open(filename, 'w') as file:
        json.dump(books, file, indent=4)

def add_book(books):
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    status = input("Enter the status (Owned, Read, Wish to Read): ")

    books.append({'title': title, 'author': author, 'status': status})
    save_library(books)
    print(f"Book '{title}' added to the library.")

def view_library(books):
    for book in books:
        print(f"\nTitle: {book['title']}, Author: {book['author']}, Status: {book['status']}")

def update_book_status(books):
    title = input("Enter the title of the book to update: ")
    new_status = input("Enter the new status (Owned, Read, Wish to Read): ")

    for book in books:
        if book['title'] == title:
            book['status'] = new_status
            save_library(books)
            print("Book status updated.")
            return

    print("Book not found in the library.")

def main():
    books = load_library()

    while True:
        action = input("\nChoose an action - Add Book (A), View Library (V), Update Status (U), Exit (E): ").upper()

        if action == 'A':
            add_book(books)

        elif action == 'V':
            view_library(books)

        elif action == 'U':
            update_book_status(books)

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
