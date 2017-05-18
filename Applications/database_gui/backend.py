"""
    Backend for the database gui
"""
import sqlite3

def create_table():
    """
        Creates the book table in the Book database
    """
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Book (Id INTEGER PRIMARY KEY, \
        Title TEXT, Author TEXT, Year INTEGER, ISBN INTEGER)")
    connection.commit()
    connection.close()

def insert_book(title, author, year, isbn):
    """
        Inserts a book into the book table
    """
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Book VALUES(NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    connection.commit()
    connection.close()

def view():
    """
        Returns all books from the book table
    """
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Book")
    rows = cursor.fetchall()
    connection.close()
    return rows

def search(title="", author="", year="", isbn=""):
    """
        Searches for a book and returns the results
    """
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Book WHERE Title = ? OR Author = ? \
        OR Year = ? OR ISBN = ?", (title, author, year, isbn))
    rows = cursor.fetchall()
    connection.close()
    return rows

def delete(id):
    """
        Deletes a book from the book database
    """
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Book WHERE Id = ?", (id,))
    connection.commit()
    connection.close()

def update(id, title, author, year, isbn):
    """
        Updates a book from the book database
    """
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE Book SET Title = ?, Author = ?, Year = ?, ISBN = ? WHERE Id = ?",
                   (title, author, year, isbn, id))
    connection.commit()
    connection.close()

create_table()
#insert_book("The Sun", "John Smith", 1918, 1231243)
#delete(3)
#update(4, "The Moon", "John Smooth", 1917, 987584)
#print(view())
#print(search(author="John Smith"))
