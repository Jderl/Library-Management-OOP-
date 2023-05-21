from book import Book

# The NonFictionBook class extends the Book class and represents a non-fiction book.
# It adds an additional attribute 'topic' and overrides the 'get_details' method to include the topic in the book details.


class NonFictionBook(Book):
    def __init__(self, title, author, isbn, topic):
        super().__init__(title, author, isbn)
        self.topic = topic

    def get_details(self):
        return f"Non-Fiction Book: Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Topic: {self.topic}"
    
