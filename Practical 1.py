class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False
        return

    def display(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        print(f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Status: {status}")
        return


class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []
        return

    def display(self):
        print(f"Patron ID: {self.patron_id}, Name: {self.name}")
        if self.borrowed_books:
            print("Borrowed Books:", ", ".join(self.borrowed_books))
        else:
            print("Borrowed Books: None")
        return


class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}
        return

    def add_book(self, book):
        if book.book_id in self.books:
            print(f"Book ID {book.book_id} already exists.")
        else:
            self.books[book.book_id] = book
            print(f"Book '{book.title}' added successfully.")
        return

    def register_patron(self, patron):
        if patron.patron_id in self.patrons:
            print(f"Patron ID {patron.patron_id} already exists.")
        else:
            self.patrons[patron.patron_id] = patron
            print(f"Patron '{patron.name}' registered successfully.")
        return

    def borrow_book(self, patron_id, book_id):
        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        if book_id not in self.books:
            print("Book not found.")
            return

        book = self.books[book_id]
        patron = self.patrons[patron_id]

        if book.is_borrowed:
            print(f"Book '{book.title}' is already borrowed.")
        else:
            book.is_borrowed = True
            patron.borrowed_books.append(book.title)
            print(f"{patron.name} borrowed '{book.title}'.")
        return

    def return_book(self, patron_id, book_id):
        if patron_id not in self.patrons or book_id not in self.books:
            print("Invalid Patron ID or Book ID.")
            return

        book = self.books[book_id]
        patron = self.patrons[patron_id]

        if book.title in patron.borrowed_books:
            book.is_borrowed = False
            patron.borrowed_books.remove(book.title)
            print(f"{patron.name} returned '{book.title}'.")
        else:
            print("This book was not borrowed by the patron.")
        return

    def display_books(self):
        print("\n===== Library Books =====")
        if not self.books:
            print("No books available.")
        else:
            for book in self.books.values():
                book.display()
        return

    def display_patrons(self):
        print("\n===== Registered Patrons =====")
        if not self.patrons:
            print("No patrons registered.")
        else:
            for patron in self.patrons.values():
                patron.display()
                print()
        return


def main():
    library = Library()

    while True:
        print("\n====== Library Management System ======")
        print("1. Add Book")
        print("2. Register Patron")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Display Books")
        print("6. Display Patrons")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            library.add_book(Book(book_id, title, author))

        elif choice == "2":
            patron_id = input("Enter Patron ID: ")
            name = input("Enter Patron Name: ")
            library.register_patron(Patron(patron_id, name))

        elif choice == "3":
            patron_id = input("Enter Patron ID: ")
            book_id = input("Enter Book ID: ")
            library.borrow_book(patron_id, book_id)

        elif choice == "4":
            patron_id = input("Enter Patron ID: ")
            book_id = input("Enter Book ID: ")
            library.return_book(patron_id, book_id)

        elif choice == "5":
            library.display_books()

        elif choice == "6":
            library.display_patrons()

        elif choice == "7":
            print("Exiting Library Management System.")
            break

        else:
            print("Invalid choice. Please try again.")
    return


if __name__ == "__main__":
    main()
