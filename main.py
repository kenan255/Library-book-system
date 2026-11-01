print("Welcome to Library System!")

books = []

while True:
    print("\n1 - Add Book")
    print("2 - Show Books")
    print("3 - Search Book")
    print("4 - Borrow Book")
    print("5 - Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter book name: ")
        books.append(name)
        print("Book added successfully!")

    elif choice == "2":
        print("Available Books:")
        for book in books:
            print(book)

    elif choice == "3":
        name = input("Enter book name: ")
        if name in books:
            print("Book found!")
        else:
            print("Book not found!")

    elif choice == "4":
        name = input("Enter book name: ")
        if name in books:
            books.remove(name)
            print("Book borrowed successfully!")
        else:
            print("Book not available!")

    elif choice == "5":
        print("Thank you for using Library System!")
        break

    else:
        p
