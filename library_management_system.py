class Book:
    def __init__(self, book_id, title, author, category):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.status = "available"

    def display_book(self):
        print("Book ID :", self.book_id)
        print("Title   :", self.title)
        print("Author  :", self.author)
        print("Category:", self.category)
        print("Status  :", self.status)

    def borrow_book(self):
        if self.status == "available":
            self.status = "borrowed"
            print("Book borrowed successfully.")
        else:
            print("Sorry! Book is not available.")

    def return_book(self):
        if self.status == "borrowed":
            self.status = "available"
            print("Book returned successfully.")
        else:
            print("Book is already available.")

    def is_available(self):
        return self.status == "available"


class Member:
    def __init__(self, member_id, name, phone_no):
        self.member_id = member_id
        self.name = name
        self.phone_no = phone_no
        self.borrowed_books = []

    def display_member(self):
        print("Member ID :", self.member_id)
        print("Name      :", self.name)
        print("Phone No  :", self.phone_no)

        if len(self.borrowed_books) == 0:
            print("Borrowed Books : None")
        else:
            print("Borrowed Books:")
            for book in self.borrowed_books:
                print("-", book.title)

    def borrow_book(self, book):
        self.borrowed_books.append(book)
        print(book.title, "borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(book.title, "returned.")
        else:
            print("This member did not borrow the book.")


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.")

    def add_member(self, member):
        self.members.append(member)
        print("Member registered successfully.")

    def display_books(self):
        if len(self.books) == 0:
            print("No books available.")
        else:
            for book in self.books:
                book.display_book()
                print("-" * 30)

    def display_members(self):
        if len(self.members) == 0:
            print("No members registered.")
        else:
            for member in self.members:
                member.display_member()
                print("-" * 30)

    def search_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def search_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def borrow_book(self, member_id, book_id):
        member = self.search_member(member_id)
        book = self.search_book(book_id)

        if member is None:
            print("Member not found.")
            return

        if book is None:
            print("Book not found.")
            return

        if book.is_available():
            book.borrow_book()
            member.borrow_book(book)
        else:
            print("Book is already borrowed.")

    def return_book(self, member_id, book_id):
        member = self.search_member(member_id)
        book = self.search_book(book_id)

        if member is None:
            print("Member not found.")
            return

        if book is None:
            print("Book not found.")
            return

        if book in member.borrowed_books:
            book.return_book()
            member.return_book(book)
        else:
            print("This member did not borrow this book.")
library = Library()

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Register Member")
    print("3. Display Books")
    print("4. Display Members")
    print("5. Search Book")
    print("6. Borrow Book")
    print("7. Return Book")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book_id = input("Book ID: ")
        title = input("Title: ")
        author = input("Author: ")
        category = input("Category: ")
        library.add_book(Book(book_id, title, author, category))

    elif choice == 2:
        member_id = input("Member ID: ")
        name = input("Name: ")
        phone = input("Phone: ")
        library.add_member(Member(member_id, name, phone))

    elif choice == 3:
        library.display_books()

    elif choice == 4:
        library.display_members()

    elif choice == 5:
        book_id = input("Enter Book ID: ")
        book = library.search_book(book_id)
        if book:
            book.display_book()
        else:
            print("Book not found.")

    elif choice == 6:
        member_id = input("Member ID: ")
        book_id = input("Book ID: ")
        library.borrow_book(member_id, book_id)

    elif choice == 7:
        member_id = input("Member ID: ")
        book_id = input("Book ID: ")
        library.return_book(member_id, book_id)

    elif choice == 8:
        print("Thank you!")
        break

    else:
        print("Invalid choice.")