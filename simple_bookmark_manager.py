import json
import os

def load_bookmarks(filename='bookmarks.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

def save_bookmarks(bookmarks, filename='bookmarks.json'):
    with open(filename, 'w') as file:
        json.dump(bookmarks, file, indent=4)

def add_bookmark(bookmarks):
    title = input("Enter the bookmark title: ")
    url = input("Enter the URL: ")
    category = input("Enter a category (optional): ")

    bookmarks.append({'title': title, 'url': url, 'category': category})
    save_bookmarks(bookmarks)
    print("Bookmark added.")

def view_bookmarks(bookmarks, category=None):
    filtered_bookmarks = [bookmark for bookmark in bookmarks if bookmark['category'] == category] if category else bookmarks
    if not filtered_bookmarks:
        print("No bookmarks found.")
        return
    for bookmark in filtered_bookmarks:
        print(f"\nTitle: {bookmark['title']}\nURL: {bookmark['url']}\nCategory: {bookmark['category']}")

def main():
    bookmarks = load_bookmarks()

    while True:
        action = input("\nChoose an action - Add (A), View (V), View by Category (C), Exit (E): ").upper()

        if action == 'A':
            add_bookmark(bookmarks)

        elif action == 'V':
            view_bookmarks(bookmarks)

        elif action == 'C':
            category = input("Enter the category to filter by: ")
            view_bookmarks(bookmarks, category)

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
