class Book:
    def __init__(self, title, author, isbn):
        self.title = title  # Set the title attribute
        self.author = author  # Set the author attribute
        self.isbn = isbn  # Set the ISBN attribute
        self.borrowed = False  # Set the borrowed attribute to False by default

    def get_details(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

    def is_borrowed(self):
        return self.borrowed

    def borrow(self):
        self.borrowed = True

    def return_book(self):
        self.borrowed = False
