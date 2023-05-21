from book import Book

# The FictionBook class extends the Book class and represents a fiction book.
# It adds an additional attribute 'genre' and overrides the 'get_details' method to include the genre in the book details.
class FictionBook(Book):
    def __init__(self, title, author, isbn, genre):
        super().__init__(title, author, isbn)
        self.genre = genre

    def get_details(self):
        return f"Fiction Book: Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Genre: {self.genre}"

