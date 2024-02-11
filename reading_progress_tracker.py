import json
import os
from datetime import datetime


def load_reading_data(filename='reading_data.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return {"books": {}, "logs": []}


def save_reading_data(data, filename='reading_data.json'):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def add_reading_log(data):
    book_title = input("Enter the book title: ")
    pages_read = int(input("Enter the number of pages read: "))
    date_read = datetime.now().strftime('%Y-%m-%d')

    if book_title not in data["books"]:
        total_pages = int(input("Enter the total number of pages in the book: "))
        data["books"][book_title] = {"total_pages": total_pages, "pages_read": 0}

    data["books"][book_title]["pages_read"] += pages_read
    data["logs"].append({"book_title": book_title, "pages_read": pages_read, "date": date_read})
    save_reading_data(data)
    print(f"Added {pages_read} pages to '{book_title}' reading log.")


def view_progress(data):
    for title, details in data["books"].items():
        print(f"\n{title}: {details['pages_read']}/{details['total_pages']} pages read")
        progress_percentage = (details['pages_read'] / details['total_pages']) * 100
        print(f"Progress: {progress_percentage:.2f}%")


def main():
    data = load_reading_data()

    while True:
        action = input("\nChoose an action - Log Reading (L), View Progress (V), Exit (E): ").upper()

        if action == 'L':
            add_reading_log(data)

        elif action == 'V':
            view_progress(data)

        elif action == 'E':
            break


if __name__ == "__main__":
    main()
