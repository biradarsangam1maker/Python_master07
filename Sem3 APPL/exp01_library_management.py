class Book:
    def __init__(self,title,book_id,book_availability = True):
        self.title=title
        self.book_id = book_id
        self.book_availability = book_availability

class Patron:
    def __init__(self,name,user_id):
        self.name = name
        self.user_id = user_id
        # Every new patron gets their own empty list
        self.backpack = []

class Library:
    def __init__(self):
        # The Library acts as the central database
        self.books = []
        self.patrons = []

    def add_book(self, new_book):
        # The library just catches the book and puts it on the shelf.
        # No inputs, no prints. Pure logic.
        self.books.append(new_book)
        return "Book added Successfully"

    def register_patron(self, new_patron):
        # Hard lesson , This is only brain not ears and eyes or mouth.
        self.patrons.append(new_patron)
        return "Patron registered Successfully"

    def borrow_book(self,patron_id,target_book_id):
        # check if given values exist in database or not
        temp_patron,temp_book = None,None
        for el in self.patrons:
            if el.user_id == patron_id:
                temp_patron = el
                break
        for el  in self.books:
            if el.book_id == target_book_id:
                temp_book = el
                break
        # if else logic for error handling.
        if temp_patron == None:
            return "Error: Patron not found"
        elif temp_book == None:
            return "Error: Book not registered in library"
        elif not temp_book.book_availability:
            return "Sorry, that book is already checked out"
        else:
            temp_patron.backpack.append(temp_book)
            temp_book.book_availability = False
            return "Book succesfully checked out"

    def return_book(self,patron_id,return_book_id):
        # check if given values exist in database or not
        temp_patron,temp_book = None,None

        for el in self.patrons:
            if el.user_id == patron_id:
                temp_patron = el
                break
        for el in self.books:
            if el.book_id == return_book_id:
                temp_book = el
                break

        #if else logic for error handling and operation manipulation
        if temp_patron is None:
            return "Error: Patron not found"
        elif temp_book is None:
            return "Error: Book not registered with library"
        # if person has more than one book in backpack and there is not your book inside it.
        elif temp_book not in temp_patron.backpack:
            return "Error: The book is not inside the backpack"
        else:
            temp_patron.backpack.remove(temp_book)
            temp_book.book_availability = True
            return "Book successfully returned"
            
my_college_library = Library()
while True:
    print("---WELCOME TO LIBRARY--- \nChoose one of the following service by entering the serial number")

    try:
        choice = int(input("1.Add Book\n2.Register Patron\n3.Borrow Book\n4.Return Book\n5.Display list of Patrons\n6.exit\nchoice: "))
        if choice == 1:
            fresh_book = Book(input("Enter the title of Book: "),int(input("Enter Book ID: ")))
            print(my_college_library.add_book(fresh_book))

        elif choice == 2:
            fresh_patron = Patron(input("Enter User name: "),int(input("User ID: ")))
            print(my_college_library.register_patron(fresh_patron))
        
        elif choice == 3:
            print(my_college_library.borrow_book(int(input("Enter Patron ID: ")),int(input("Enter book ID of book you want to issue: "))))

        elif choice == 4:
            print(my_college_library.return_book(int(input("Enter Patron ID: ")),int(input("Enter book ID of book you want to return: "))))
        
        elif choice == 6:
            break
        
        elif choice == 5:
            print(my_college_library.patrons)
        else:
            print("Error: Please enter valid service number.")

    except ValueError:
        print("Error:Please Enter valid input")
