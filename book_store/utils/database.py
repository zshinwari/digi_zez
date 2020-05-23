""""
Program interface file which interacts with the backend database and the user interface app.py
"""
import sqlite3
from utils.database_connection import DatabaseConnection


def create_table():
    with DatabaseConnection('database.db') as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books (title text PRIMARY KEY, author text, read integer default 0)')

#create_table()


def insert_data(title, author):
    with DatabaseConnection('database.db') as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO books (title, author) VALUES (?, ?)', (title, author))


#insert_data("Intro to Python", "Python")


def list_data():
    with DatabaseConnection('database.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM books')
        rows = cursor.fetchall()
        return rows

#list_data()


def mark_book_read(title):
    with DatabaseConnection('database.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f"UPDATE books SET read = 1 where title = '{title}'")

#mark_book_read('Clean Code')


def delete_book(title):
    with DatabaseConnection('database.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM books where title = '{title}'")
        connection.commit()
