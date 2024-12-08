def view_books(books):
    if books:
        print("\nAvailable books: ")
        for book in books:
            print(f"- {book}")
    else:
        print("\nNo books are currently available.")


def borrow_book(books, book_name):
    if book_name in books:
        books.remove(book_name)
        print(f"\nYou have borrowed: {book_name}")
    else:
        print(f"\nSorry, the book '{book_name}' is not available.")


def return_book(books, book_name):
    if book_name not in books:
        books.append(book_name)
        print(f"\nThank you for returning: {book_name}")
    else:
        print(f"\nThe book '{book_name}' is already in library.")


def main():
    books = ["Python Basics", "Data Science 101", "AI for Beginners"]

    while True:
        print("\nWelcome to library management system")
        print("1. View Available books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Quit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            view_books(books)
        elif choice == "2":
            book_name = input("Enter the name of the book to borrow: ")
            borrow_book(books, book_name)
        elif choice == "3":
            book_name = input("Enter the name of the book to return: ")
            return_book(books, book_name)
        elif choice == "4":
            print("Thank you for using the Library Management System.")
            break
        else:
            print("Invalid option. Please try again!")


if __name__ == "__main__":
    main()
