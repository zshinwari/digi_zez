from app import books
from parsers.book import Parsers

USER_CHOICE = '''Enter one of the following
- 'b' to look at 5-star books
- 'c' to look at the cheapest books
- 'n' to just get the next available book on the page
- 'q' to exit
Enter your choice: '''


def cheapest_book_func():
    cheapest_book = sorted(books, key=lambda x: x.price, reverse=True)
    for book in cheapest_book[:10]:
        print(book)


def best_book_func():
    best_book = sorted(books, key=lambda x: x.star_rating, reverse=True)
    for book in best_book[:10]:
        print(book)


gen = (book for book in books)


def next_available():
    print(next(gen))


funcs = {'c': cheapest_book_func,
         'b': best_book_func,
         'n': next_available}


def menu():
    question = input(f"{USER_CHOICE}:")
    while question != 'q':
        if question in ('c', 'b', 'n'):
            funcs[question]()
        else:
            print('Invalid option, please try agian')
        question = input(f"{USER_CHOICE}:")













