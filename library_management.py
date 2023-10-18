import sqlite3

# Create a connection to the database
conn = sqlite3.connect('library.db')
c = conn.cursor()

# Create a table for books
c.execute('''CREATE TABLE IF NOT EXISTS books
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             title TEXT NOT NULL,
             author TEXT NOT NULL,
             year INTEGER NOT NULL)''')
conn.commit()


def add_book(title, author, year):
    # Add a new book to the database
    c.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", (title, author, year))
    conn.commit()
    print("Book added successfully!")


def display_books():
    # Display all the books in the library
    c.execute("SELECT * FROM books")
    books = c.fetchall()
    if len(books) == 0:
        print("No books found in the library.")
    else:
        for book in books:
            print("ID: {}, Title: {}, Author: {}, Year: {}".format(book[0], book[1], book[2], book[3]))


def search_book(title):
    # Search for a book by title
    c.execute("SELECT * FROM books WHERE title=?", (title,))
    books = c.fetchall()
    if len(books) == 0:
        print("No books found with the title '{}'.".format(title))
    else:
        for book in books:
            print("ID: {}, Title: {}, Author: {}, Year: {}".format(book[0], book[1], book[2], book[3]))


def delete_book(book_id):
    # Delete a book from the library
    c.execute("DELETE FROM books WHERE id=?", (book_id,))
    conn.commit()
    print("Book deleted successfully!")


# Main program loop
while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        year = int(input("Enter the year of publication: "))
        add_book(title, author, year)

    elif choice == '2':
        display_books()

    elif choice == '3':
        title = input("Enter the title of the book to search: ")
        search_book(title)

    elif choice == '4':
        book_id = int(input("Enter the ID of the book to delete: "))
        delete_book(book_id)

    elif choice == '0':
        break

    else:
        print("Invalid choice. Please try again.")

# Close the database connection
conn.close()
