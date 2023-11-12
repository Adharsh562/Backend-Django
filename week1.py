class Library:
    def __init__(self, books):
        self.books = books

    def display_available_books(self):
        print("Available Books:")
        for book in self.books:
            if book.available:
                print(book.title)

    def lend_book(self, book_title, user):
        for book in self.books:
            if book.title == book_title and book.available:
                book.borrower = user
                book.available = False
                print(f"{book_title} has been borrowed by {user}.")
                return
        print("Book not available.")

    def return_book(self, book_title):
        for book in self.books:
            if book.title == book_title and not book.available:
                book.borrower = None
                book.available = True
                print(f"{book_title} has been returned.")
                return
        print("Invalid book title or book not borrowed.")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
        self.borrower = None

if __name__ == "__main__":
    book1 = Book("Python Programming", "John Smith")
    book2 = Book("Data Structures and Algorithms", "Alice Johnson")
    book3 = Book("Introduction to AI", "Bob Brown")

    library = Library([book1, book2, book3])

    while True:
        print("\nLibrary Menu:")
        print("1. Display Available Books")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            library.display_available_books()
        elif choice == "2":
            book_title = input("Enter the title of the book you want to borrow: ")
            user = input("Enter your name: ")
            library.lend_book(book_title, user)
        elif choice == "3":
            book_title = input("Enter the title of the book you want to return: ")
            library.return_book(book_title)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
