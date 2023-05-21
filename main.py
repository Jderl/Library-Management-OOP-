from library import Library
from fiction_book import FictionBook
from nonfiction_book import NonFictionBook
from member import Member

# Function to display the library management menu options
def display_library_menu():
    print("\n")
    print("===================================")
    print("==== Library Management System ====")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Display Available Books")
    print("4. Display Members")
    print("0. Exit")
    print("===================================")
    print("\n")

# Function to display the member menu options
def display_member_menu():
    print("\n")
    print("===================================")
    print("======== Member Actions ============")
    print("5. Borrow Book")
    print("6. Return Book")
    print("7. Display Borrowed Books")
    print("0. Exit")
    print("===================================")
    print("\n")

# Function to add a book to the library
def add_book(library):
    print("======= [1] ADDING BOOK ===================")
    # Get book details from the user
    title = input("Enter the title: ")
    author = input("Enter the author: ")
    isbn = input("Enter the ISBN: ")
    book_type = input("Enter the book type ([1] - Fiction, [2] - Non-Fiction): ")

    if book_type == "1":
        # Get additional genre for fiction books
        genre = input("Enter the genre: ")
        book = FictionBook(title, author, isbn, genre)
        print("\n")
    elif book_type == "2":
        # Get additional topic for non-fiction books
        topic = input("Enter the topic: ")
        book = NonFictionBook(title, author, isbn, topic)
        print("\n")
    else:
        print("\n")
        print("Invalid book type.")
        return

    # Add the book to the library
    library.add_book(book)
    print("Book added successfully.")

# Function to remove a book from the library
def remove_book(library):
    print("\n")
    print("======= [2] REMOVING BOOK ===================")
    # Display available books in the library
    display_available_books(library)
    isbn = input("Enter the ISBN of the book to remove: ")

    # Find the book in the library and remove it
    for book in library.books:
        if book.isbn == isbn:
            library.remove_book(book)
            print("\n")
            print(f"Book with ISBN {isbn} removed successfully.")
            return

    print("Book not found.")
    print("\n")

# Function to display the available books in the library
def display_available_books(library):
    print("\n")
    print("=======  DISPLAYING AVAILABLE BOOKS ===================")
    library.display_available_books()
    print("\n")

# Function to display the members of the library
def display_members(library):
    print("\n")
    print("======= [4] DISPLAYING MEMBERS ===================")
    library.display_members()
    print("\n")

# Function to borrow a book from the library
def borrow_book(library, member):
    print("======= [5] BORROWING BOOKS =================== \n")
    # Display available books in the library
    display_available_books(library)

    # Get ISBN of the book to borrow from the user
    print("\n")
    isbn = input("Enter the ISBN of the book to borrow: ")

    # Find the book in the library and check if it is available for borrowing
    for book in library.books:
        if book.isbn == isbn:
            if not book.is_borrowed():
                # Borrow the book and add it to the member's borrowed books
                member.borrow_book(book)
                print("\n")
                print("Book borrowed successfully.")
                return
            else:
                print("\n")
                print("Book is already borrowed.")
                return

    print("Book not found.")
    print("\n")

# Function to return a borrowed book to the library
def return_book(library, member):
    print("======= [6] RETURNING BOOK =================== \n")
    # Display the member's borrowed books
    print("Borrowed Books:")
    member.display_borrowed_books()

    print("\n")
    # Get ISBN of the book to return from the user
    isbn = input("Enter the ISBN of the book to return: ")

    # Find the book in the member's borrowed books and return it
    for book in member.borrowed_books:
        if book.isbn == isbn:
            member.return_book(book)
            print("\n")
            print("Book returned successfully.")
            return

    print("Book not found in your borrowed books. " )
  
    print("\n")

# Function to create dummy data for testing
def create_dummy_data(library):
    # Data for testing
    book1 = FictionBook("The Great Gatsby", "F. Scott Fitzgerald", "1", "Novel")
    book2 = FictionBook("Rebecca", "Daphne du Maurier", "2", "Mystery")
    book3 = FictionBook("The Maid: A Novel", "Nita Prose", "3", "Mystery")

    # Adding fiction books to the library
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    book4 = NonFictionBook("Sapiens: A Brief History of Humankind", "Yuval Noah Harari", "4", "History")
    book5 = NonFictionBook("Silent Spring", "Rachel Carson", "5", "Science")
    book6 = NonFictionBook("Cosmos", "Carl Sagan", "6", "Science")

    # Adding non-fiction books to the library
    library.add_book(book4)
    library.add_book(book5)
    library.add_book(book6)

def main():
    # Create a library object
    library = Library("My Library")

    # Create a member object
    member = Member("John")

    # Add the member to the library
    library.add_member(member)

    # Create dummy data for testing
    create_dummy_data(library)

    while True:
        # Display menu to the user
        print("\n")
        print("===================================")
        print("======= Library System Menu =======")
        print("1. Library Management Menu")
        print("2. Member Menu")
        print("0. Exit")
        print("===================================")
        print("\n")

        # Get user's choice
        choice = input("Enter your choice: ")

        # Perform actions based on user's choice
        if choice == "1":
            while True:
                # Display library management menu to the user
                display_library_menu()

                # Get user's choice for library management
                library_choice = input("Enter your choice: ")

                if library_choice == "1":
                    add_book(library)
                elif library_choice == "2":
                    remove_book(library)
                elif library_choice == "3":
                    display_available_books(library)
                elif library_choice == "4":
                    display_members(library)
                elif library_choice == "0":
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == "2":
            while True:
                # Display member menu to the user
                display_member_menu()

                # Get user's choice for member actions
                member_choice = input("Enter your choice: ")

                if member_choice == "5":
                    borrow_book(library, member)
                elif member_choice == "6":
                    return_book(library, member)
                elif member_choice == "7":
                    member.display_borrowed_books()
                elif member_choice == "0":
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
