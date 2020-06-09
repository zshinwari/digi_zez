"""
User interface program that interacts with program interface by importing the packages.
"""
from utils import database

database.create_table()

def add_books_prompt():
    title = input("Enter Title: ")
    author = input("Enter book author: ")
    database.insert_data(title, author)


def list_books_prompt():
    rows = database.list_data()
    try:
        for row in rows:
            read = 'Yes' if row[2] else 'No'
            print(f"{row[0]} by {row[1]} - Read: {read}")
    except Exception as e:
        print("Error", e)

def mark_book_as_read_prompt():
    title = input("Enter title of the book you read: ")
    database.mark_book_read(title)


def delete_books_prompt():
    title = input("Enter the title of the book you wish to delete: ")
    database.delete_book(title)


USER_CHOICES = """
        Enter:
        'a' to add a new book
        'l' to list all books
        'r' to mark the book as read
        'd' to delete a book
        'q' to quit
        """


func = {'a': add_books_prompt,
        'l': list_books_prompt,
        'r': mark_book_as_read_prompt,
        'd': delete_books_prompt}


def menu():
    choice = input(f"{USER_CHOICES} ")
    while choice != 'q':
        if choice in func.keys():
            select = func[choice]
            select()
        else:
            print("Invalid argument, please try again")
        choice = input(f"{USER_CHOICES} ")

menu()