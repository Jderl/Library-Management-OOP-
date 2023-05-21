class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []  # Initialize an empty list to store members

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def display_available_books(self):
        print("\n======= Available Books ===================")
        for book in self.books:
            if not book.is_borrowed():
                print(book.get_details())
        print("\n")

    def add_member(self, member):
        self.members.append(member)  # Add the member to the library

    def remove_member(self, member):
        self.members.remove(member)  # Remove the member from the library

    def display_members(self):
        print("\n======= Members ===================")
        for member in self.members:
            print(member.name)
        print("\n")