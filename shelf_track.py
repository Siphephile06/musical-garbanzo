import os
import sqlite3

'''
shelf_track: A simple bookstore inventory management program.
Allows a clerk to add, update, delete, and search for books.
Books are stored in a text file database (books_db.txt).
'''

DB_FILE = 'books_db.txt'


# define a funtion to add books to the database
def add_book():
    '''
    Add a new book to the database.
    '''
    with open(DB_FILE, 'a') as db:
        title = input("Enter the book title: ")
        author = input("Enter the book author: ")
        
        # Validate year input
        while True:
            year = input("Enter the year of publication: ")
            if year.isdigit() and 1000 <= int(year) <= 2100:
                break
            else:
                print("Please enter a valid year (e.g., 1999).")
        
        isbn = input("Enter the ISBN number: ")
        db.write(f"{title},{author},{year},{isbn}\n")
    print(f"Book '{title}' added successfully.")
    return


# define a function to update books in the database
def update_book():
    '''
    Update an existing book in the database.'''
    title = input("Enter the book title to update: ")
    
    # Read the database file
    with open(DB_FILE, 'r') as db:
        books = db.readlines()
    with open(DB_FILE, 'w') as db:
        # Loop through each book in the database
        for book in books:
            
            details = book.strip().split(',')
            # If the title matches, ask for new details
            if details[0].lower() == title.lower():
                print(f"Updating book: {details[0]}")
                
                new_title = input(
                    "Enter new title (leave blank to keep current): "
                ) or details[0]
                
                new_author = input("Enter new author "
                                   "(leave blank to keep current): "
                ) or details[1]
                
                new_year = input("Enter new year "
                                 "(leave blank to keep current): "
                ) or details[2]
                
                new_isbn = input("Enter new ISBN "
                                 "(leave blank to keep current): "
                ) or details[3]
                
                db.write(f"{new_title},{new_author},{new_year},{new_isbn}\n")
                print(f"Book '{title}' updated successfully.")
            else:
                # Write the unchanged book details
                db.write(book)
    return


# define a function to delete books from the database
def delete_book():
    '''
    Delete an existing book from the database.'''
    # Ask user for the title of the book to delete
    title = input("Enter the book title to delete: ")
    # Read the database file
    with open(DB_FILE, 'r') as db:
        books = db.readlines()
    # Open the database file in write mode
    with open(DB_FILE, 'w') as db:
        found = False
        # Loop through each book in the database
        for book in books:
            details = book.strip().split(',')
            # If the title matches, skip writing it to the file
            if details[0].lower() == title.lower():
                found = True
                print(f"Book '{title}' deleted successfully.")
            else:
                db.write(book)
        if not found:
            print(f"Book '{title}' not found.")
    return


# define a function to search for books in the database
def search_book():
    '''
    Search for a book in the database by title.'''
    # Ask user for the title of the book to search
    title = input("Enter the book title to search: ")
    # Read the database file
    with open(DB_FILE, 'r') as db:
        books = db.readlines()
    found = False
    # Loop through each book in the database
    for book in books:
        details = book.strip().split(',')
        # If the title matches, print the book details
        if details[0].lower() == title.lower():
            found = True
            print(
                f"Book found: Title: {details[0]}, Author: {details[1]}, "
                f"Year: {details[2]}, "
                f"ISBN: {details[3]}"
            )
            break
    if not found:
        print(f"Book '{title}' not found.")
    return


# define a function to display the menu
def display_menu():
    print("\nBookstore Inventory Management")
    print("1. Add Book")
    print("2. Update Book")
    print("3. Delete Book")
    print("4. Search Book")
    print("5. Exit")


# define the main function
def main():
    '''
    Main function to run the bookstore inventory management program.'''
    # Check if the database file exists, if not create it
    if not os.path.exists(DB_FILE):
        open(DB_FILE, 'w').close()  # Create an empty file
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            add_book()
        elif choice == '2':
            update_book()
        elif choice == '3':
            delete_book()
        elif choice == '4':
            search_book()
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Create a database called 'ebbokstore'
def create_database():
    ''' Create a SQLite database for the ebookstore. '''
    conn = sqlite3.connect('ebookstore.db')
    cursor = conn.cursor()

    cursor.execute('PRAGMA foreign_keys = ON')
    # Create a table for books
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            authorID INTEGER NOT NULL,
            qty INTEGER NOT NULL,
            FOREIGN KEY (authorID) REFERENCES authors(id)
        )
    ''')
    # Create a table for authors
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            country TEXT NOT NULL
    )
    ''')
    
    cursor.execute('''
    INSERT INTO authors (id, name, country) VALUES
        (1290, 'Charles Dickens', 'England'),
        (8937, 'J.K. Rowling', 'England'),
        (2356, 'C.S. Lewis', 'Ireland'),
        (6380, 'J.R.R. Tolkien', 'South Africa'),
        (5620, 'Lewis Carroll', 'England')
    ''')
            
    # Shorter version of inserting initial books into the database

    books = [
        (3001, 'A Tale of Two Cities ', 1290, 30),
        (3002, "Harry Potter and the Philosopher's Stone", 8937, 40),
        (3003, 'The Lion, the Witch and the Wardrobe', 2356, 25),
        (3004, 'The Lord of the Rings', 6380, 37),
        (3005, 'Alice’s Adventures in Wonderland ', 5620, 12)
    ]
    cursor.executemany('''
        INSERT INTO books (id, title, authorID, qty)
        VALUES (?, ?, ?, ?)
    ''', books)
    # Commit the changes and close the connection
    conn.commit()
    conn.close()


# Present menu for the database operations
def display_db_menu():
    print("\nE-Bookstore Database Management")
    print("1. Enter Book")
    print("2. Update Book")
    print("3. Delete Book")
    print("4. Search Book")
    print("5. View details of all Books")
    print("6. Add Author")  
    print("0. Exit")


# Function to enter a new book into the database
def enter_book():
    ''' Enter a new book into the database. '''
    show_authors()
    conn = sqlite3.connect('ebookstore.db')
    cursor = conn.cursor()
    title = input("Enter book title: ")

    # Validate authorID input
    while True:
        authorID_input = input("Enter author ID from the list above: ")
        if authorID_input.isdigit():
            authorID = int(authorID_input)
            break
        else:
            print("Please enter a valid numeric author ID.")

    # Validate quantity input
    while True:
        qty_input = input("Enter quantity: ")
        if qty_input.isdigit():
            qty = int(qty_input)
            break
        else:
            print("Please enter a valid numeric quantity.")

    try:
        cursor.execute('''
            INSERT INTO books (title, authorID, qty)
            VALUES (?, ?, ?)
        ''', (title, authorID, qty))
        conn.commit()
        print(f"Book '{title}' added successfully.")
    except sqlite3.IntegrityError:
        print("Error: Author ID does not exist.")
        print("Please add the author first or choose a valid ID.")
    finally:
        conn.close()
    return


# Function to update an existing book in the database
def update_book_db():
    ''' Update an existing book in the database. '''
    # Connect to the database
    conn = sqlite3.connect('ebookstore.db')
    cursor = conn.cursor()

    # Validate book_id input
    try:
        while True:
            book_id_input = input("Enter book ID to update: ")
            if book_id_input.isdigit():
                book_id = int(book_id_input)
                break
            else:
                print("Please enter a valid numeric book ID.")
    except FileNotFoundError:
        print("Book ID not found. Please try again.")
        conn.close()
        return

    title = input("Enter new book title (leave blank to keep current): ")
    authorID = input("Enter new author ID (leave blank to keep current): ")
    qty = input("Enter new quantity (leave blank to keep current): ")

    # Build the update query dynamically
    fields = []
    params = []
    if title:
        fields.append("title = ?")
        params.append(title)
    if authorID:
        try:
            fields.append("authorID = ?")
            params.append(int(authorID))
        except ValueError:
            print("Invalid author ID. Please enter a valid integer.")
            conn.close()
            return
    if qty:
        try:
            fields.append("qty = ?")
            params.append(int(qty))
        except ValueError:
            print("Invalid quantity. Please enter a valid integer.")
            conn.close()
            return
    if not fields:
        print("No updates provided.")
        conn.close()
        return

    query = f"UPDATE books SET {', '.join(fields)} WHERE id = ?"
    params.append(book_id)
    cursor.execute(query, tuple(params))
    conn.commit()
    conn.close()
    print(f"Book with ID {book_id} updated successfully.")


# Function to update book in the author table
def update_author_db():
    ''' Update an existing author in the database. '''
    # Connect to the database
    conn = sqlite3.connect('ebookstore.db')
    cursor = conn.cursor()
    author_id = int(input("Enter book ID to update: "))
    name = input("Enter new author name (leave blank to keep current): ")
    country = input("Enter new author country (leave blank to keep current): ")
    # Build the update query dynamically
    fields = []
    params = []
    if name:
        fields.append("name = ?")
        params.append(name)
    if country:
        fields.append("country = ?")
        params.append(country)
    if not fields:
        print("No updates provided.")
        conn.close()
        return
    query = f"UPDATE authors SET {', '.join(fields)} WHERE id = ?"
    params.append(author_id)
    cursor.execute(query, tuple(params))
    conn.commit()
    conn.close()
    print(f"Author with ID {author_id} updated successfully.")


# Function to delete a book from the database
def delete_book_db():
    ''' Delete a book from the database. '''
    conn = sqlite3.connect('ebookstore.db')
    cursor = conn.cursor()
    try:
        while True:
            book_id_input = input("Enter book ID to delete: ")
            if book_id_input.isdigit():
                book_id = int(book_id_input)
                break
            else:
                print("Please enter a valid numeric book ID.")
    except FileNotFoundError:
        print("Book ID not found. Please try again.")
    try:
        cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
    except sqlite3.Error as e:
        print(f"Error deleting book: {e}")
        conn.close()
        return
    conn.commit()
    conn.close()
    print(f"Book with ID {book_id} deleted successfully.")


# Function to search for a book in the database
def search_book_db():
    ''' Search for a book in the database by title. '''
    conn = sqlite3.connect('ebookstore.db')
    cursor = conn.cursor()
    title = input(
        "Enter book title to search: "
    )
    cursor.execute('SELECT * FROM books WHERE title LIKE ?', ('%' + title + '%',))
    results = cursor.fetchall()
    if results:
        print("Books found:")
        for row in results:
            print(
                f"ID: {row[0]}, Title: {row[1]}, "
                f"Author ID: {row[2]}, "
                f"Quantity: {row[3]}"
            )
    else:
        print("No books found with that title.")
    conn.close()


# Function to view details of all books in the database
def view_all_books():
    """
    Display all books with their title, author name, country, and quantity.
    """
    conn = sqlite3.connect('ebookstore.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT books.title, authors.name, authors.country, books.qty
        FROM books
        INNER JOIN authors ON books.authorID = authors.id
    ''')
    results = cursor.fetchall()
    if results:
        print("\nAll Books in Inventory:")
        print("-" * 40)
        for row in results:
            print(f"Title   : {row[0]}")
            print(f"Author  : {row[1]}")
            print(f"Country : {row[2]}")
            print(f"Quantity: {row[3]}")
            print("-" * 40)
    else:
        print("No books found in the database.")
    conn.close()


# Function to display all authors with their IDs and countries
def show_authors():
    """Display all authors with their IDs and countries."""
    conn = sqlite3.connect('ebookstore.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, country FROM authors')
    authors = cursor.fetchall()
    print("\nAvailable Authors:")
    for author in authors:
        print(f"ID: {author[0]}, Name: {author[1]}, Country: {author[2]}")
    conn.close()


# Function to add a new author to the database
def add_author():
    """Add a new author to the database."""
    name = input("Enter author name: ")
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        # Check if author exists
        cursor.execute("SELECT id FROM authors WHERE name = ?", (name,))
        result = cursor.fetchone()
        if result:
            print("Author already exists.")
        else:
            # Insert new author
            cursor.execute("INSERT INTO authors (name) VALUES (?)", (name,))
            conn.commit()
            print("Author added successfully.")


# Function to get all authors from the database
def get_authors():
    # Using context manager for automatic connection closure
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors")
        authors = cursor.fetchall()
    return authors


# Main function to run the database management program
def main_db():
    ''' Main function to run the database management program. '''
    # Check if the database file exists, if not create it
    while True:
        display_db_menu()
        choice = input("Enter your choice (0-5): ")
        if choice == '1':
            enter_book()
        elif choice == '2':
            update_book_db()
            update_author_db()
        elif choice == '3':
            delete_book_db()
        elif choice == '4':
            search_book_db()
        elif choice == '5':
            view_all_books()
        elif choice == '6':
            add_author()
        elif choice == '0':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    print("Welcome to Shelf Track Bookstore Management!")
    print("Choose your storage method:")
    print("1. Text file (books_db.txt)")
    print("2. SQLite database (ebookstore.db)")
    method = input("Enter 1 or 2: ").strip()

    if method == "1":
        main()
    elif method == "2":
        # Check if the database exists, if not, offer to create it
        if not os.path.exists("ebookstore.db"):
            print("Database file 'ebookstore.db' not found.")
            create = input("Would you like to create and initialize the database now? (y/n): ").strip().lower()
            if create == "y":
                create_database()
                print("Database created and initialized.")
            else:
                print("Cannot continue without a database. Exiting.")
                exit()
        main_db()
    else:
        print("Invalid selection. Exiting.")







