
class Book:
    def __init__(self, title, book_id):
        self.title = title
        self.book_id = book_id
        self.available = True


class Patron:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.books = []


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)
        return "Book added successfully"

    def register_patron(self, patron):
        self.patrons.append(patron)
        return "Patron registered successfully"

    def borrow_book(self, user_id, book_id):
        for patron in self.patrons:
            if patron.user_id == user_id:
                for book in self.books:
                    if book.book_id == book_id:
                        if book.available:
                            book.available = False
                            patron.books.append(book)
                            return "Book borrowed successfully"
                        else:
                            return "Book is already borrowed"
                return "Book not found"
        return "Patron not found"

    def return_book(self, user_id, book_id):
        for patron in self.patrons:
            if patron.user_id == user_id:
                for book in patron.books:
                    if book.book_id == book_id:
                        book.available = True
                        patron.books.remove(book)
                        return "Book returned successfully"
                return "Book not borrowed by this patron"
        return "Patron not found"

    def display_patrons(self):
        for patron in self.patrons:
            print(patron.name, patron.user_id)


library = Library()

while True:
    print("\n--- LIBRARY MANAGEMENT SYSTEM ---")
    print("1. Add Book")
    print("2. Register Patron")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Display Patrons")
    print("6. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            title = input("Enter book title: ")
            book_id = int(input("Enter book ID: "))
            book = Book(title, book_id)
            print(library.add_book(book))

        elif choice == 2:
            name = input("Enter patron name: ")
            user_id = int(input("Enter user ID: "))
            patron = Patron(name, user_id)
            print(library.register_patron(patron))

        elif choice == 3:
            user_id = int(input("Enter patron ID: "))
            book_id = int(input("Enter book ID: "))
            print(library.borrow_book(user_id, book_id))

        elif choice == 4:
            user_id = int(input("Enter patron ID: "))
            book_id = int(input("Enter book ID: "))
            print(library.return_book(user_id, book_id))

        elif choice == 5:
            library.display_patrons()

        elif choice == 6:
            print("Thank you!")
            break

        else:
            print("Enter a valid choice")

    except ValueError:
        print("Please enter a valid number")
