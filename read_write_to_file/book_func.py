# Completed project of saving data to a list
list_of_book = []
USER_CHOICES = """
        Enter:
        'a' to add a new book
        'l' to list all books
        'r' to mark the book as read
        'd' to delete a book
        'q' to quit
        """

def add_books():
    title = input("Enter Title: ")
    author = input("Enter book author: ")
    return list_of_book.append({"title": title, "author": author, "read": False})

def list_books():
    for book in list_of_book:
        print(f"Title is {book['title']} and Author is {book['author']}, book read={book['read']}")

def mark_book_as_read():
    m = input("Enter Title of the book you read: ")
    for book in list_of_book:
        if m == book['title']:
            book['read'] = True

def delete_books():
    global list_of_book
    d = input("Title of the book you wish to delete: ")
    list_of_book = [book for book in list_of_book if book['title'] != n]


func = {'a': add_books,
        'l': list_books,
        'r': mark_book_as_read,
        'd': delete_books}

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

