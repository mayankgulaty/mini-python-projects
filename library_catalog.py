class LibraryCatalog:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, genre, rating):
        self.books.append({
            'title': title,
            'author': author,
            'genre': genre,
            'rating': rating
        })

    def display_books(self):
        for book in self.books:
            print(f"{book['title']} by {book['author']}, Genre: {book['genre']}, Rating: {book['rating']}")

    def search_books(self, search_term):
        found_books = [book for book in self.books if search_term.lower() in book['title'].lower() or
                       search_term.lower() in book['author'].lower() or
                       search_term.lower() in book['genre'].lower()]
        for book in found_books:
            print(f"{book['title']} by {book['author']}, Genre: {book['genre']}, Rating: {book['rating']}")


def main():
    catalog = LibraryCatalog()

    while True:
        print("\nPersonal Library Catalog")
        action = input("Choose an action - Add (A), View (V), Search (S), Exit (E): ").upper()

        if action == 'A':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            genre = input("Enter book genre: ")
            rating = input("Enter your rating (1-5): ")
            catalog.add_book(title, author, genre, rating)

        elif action == 'V':
            catalog.display_books()

        elif action == 'S':
            search_term = input("Enter a search term (title, author, or genre): ")
            catalog.search_books(search_term)

        elif action == 'E':
            break


if __name__ == "__main__":
    main()
