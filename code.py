class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.id = book_id
        self.checked_out = False

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_id(self):
        return self.id

    def is_checked_out(self):
        return self.checked_out

    def check_out(self):
        self.checked_out = True

    def check_in(self):
        self.checked_out = False


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print("Library Catalog:")
        for book in self.books:
            status = "(Checked out)" if book.is_checked_out() else "(Available)"
            print(f"Title: {book.get_title()}, Author: {book.get_author()}, ID: {book.get_id()} {status}")

    def check_out_book(self, book_id):
        for book in self.books:
            if book.get_id() == book_id:
                if not book.is_checked_out():
                    book.check_out()
                    print(f"Book '{book.get_title()}' checked out successfully.")
                else:
                    print(f"Book '{book.get_title()}' is already checked out.")
                return
        print(f"Book with ID {book_id} not found.")

    def check_in_book(self, book_id):
        for book in self.books:
            if book.get_id() == book_id:
                if book.is_checked_out():
                    book.check_in()
                    print(f"Book '{book.get_title()}' checked in successfully.")
                else:
                    print(f"Book '{book.get_title()}' is not checked out.")
                return
        print(f"Book with ID {book_id} not found.")


# Main Program
library = Library()

# Adding books to the library
library.add_book(Book("The Catcher in the Rye", "J.D. Salinger", 101))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee", 102))
library.add_book(Book("1984", "George Orwell", 103))
library.add_book(Book("Pride and Prejudice", "Jane Austen", 104))

# Display all books in the library
library.display_books()

# Example of checking out and checking in a book
library.check_out_book(102)
library.check_out_book(103)
library.check_in_book(103)

# Display updated book status
library.display_books()
