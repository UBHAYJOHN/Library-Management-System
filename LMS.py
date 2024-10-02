# Library Management System

class Book:
    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"ID: {self.book_id} | Title: {self.title} | Author: {self.author} | Year: {self.year}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_id, title, author, year):
        book = Book(book_id, title, author, year)
        self.books.append(book)
        print(f"Book '{title}' added successfully!")

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("\nList of Books in the Library:")
            for book in self.books:
                print(book)

    def search_by_title(self, title):
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        if found_books:
            print("\nSearch Results:")
            for book in found_books:
                print(book)
        else:
            print(f"No books found with the title '{title}'.")

    def search_by_author(self, author):
        found_books = [book for book in self.books if author.lower() in book.author.lower()]
        if found_books:
            print("\nSearch Results:")
            for book in found_books:
                print(book)
        else:
            print(f"No books found by the author '{author}'.")


def main():
    library = Library()

    while True:
        print("\nLibrary Management System Menu:")
        print("1. Add a Book")
        print("2. Display All Books")
        print("3. Search Book by Title")
        print("4. Search Book by Author")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            book_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            year = input("Enter Publication Year: ")
            library.add_book(book_id, title, author, year)

        elif choice == '2':
            library.display_books()

        elif choice == '3':
            title = input("Enter Book Title to Search: ")
            library.search_by_title(title)

        elif choice == '4':
            author = input("Enter Author Name to Search: ")
            library.search_by_author(author)

        elif choice == '5':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
