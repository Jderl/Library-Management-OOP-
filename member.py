class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []  # Initialize an empty list to store borrowed books

    def borrow_book(self, book):
        if book.is_borrowed():
            print("Book is already borrowed.")
        else:
            book.borrow()
            self.borrowed_books.append(book)  # Add the borrowed book to the member's list

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)  # Remove the returned book from the member's list
        else:
            print("You haven't borrowed this book.")

    def display_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name}'s borrowed books:")
            for book in self.borrowed_books:
                print(book.get_details())
        else:
            print(f"{self.name} has not borrowed any books.")
