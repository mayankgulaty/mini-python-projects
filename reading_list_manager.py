import json
import os

def load_books(filename='books.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

def save_books(books, filename='books.json'):
    with open(filename, 'w') as file:
        json.dump(books, file, indent=4)

def add_book(books):
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    status = input("Enter the reading status (Want to Read, Reading, Completed): ")

    books.append({'title': title, 'author': author, 'status': status})
    save_books(books)
    print("Book added to the reading list.")

def view_books(books):
    for book in books:
        print(f"\nTitle: {book['title']}\nAuthor: {book['author']}\nStatus: {book['status']}")

def update_book_status(books):
    title = input("Enter the title of the book to update: ")
    new_status = input("Enter the new reading status: ")

    for book in books:
        if book['title'] == title:
            book['status'] = new_status
            save_books(books)
            print("Book status updated.")
            return

    print("Book not found in the reading list.")

def main():
    books = load_books()

    while True:
        action = input("\nChoose an action - Add Book (A), View Books (V), Update Status (U), Exit (E): ").upper()

        if action == 'A':
            add_book(books)

        elif action == 'V':
            view_books(books)

        elif action == 'U':
            update_book_status(books)

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
