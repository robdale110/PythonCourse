"""
    Backend for the database gui
"""
import sqlite3

class Database(object):
    """
        Class for interacting with the database
    """

    def __init__(self, db):
        """
            Creates the book table in the Book database
        """
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Book (Id INTEGER PRIMARY KEY, \
            Title TEXT, Author TEXT, Year INTEGER, ISBN INTEGER)")
        self.connection.commit()

    def insert_book(self, title, author, year, isbn):
        """
            Inserts a book into the book table
        """
        self.cursor.execute("INSERT INTO Book VALUES(NULL, ?, ?, ?, ?)",
                            (title, author, year, isbn))
        self.connection.commit()

    def view(self):
        """
            Returns all books from the book table
        """
        self.cursor.execute("SELECT * FROM Book")
        rows = self.cursor.fetchall()
        return rows

    def search(self, title="", author="", year="", isbn=""):
        """
            Searches for a book and returns the results
        """
        self.cursor.execute("SELECT * FROM Book WHERE Title = ? OR Author = ? \
            OR Year = ? OR ISBN = ?", (title, author, year, isbn))
        rows = self.cursor.fetchall()
        return rows

    def delete(self, id):
        """
            Deletes a book from the book database
        """
        self.cursor.execute("DELETE FROM Book WHERE Id = ?", (id,))
        self.connection.commit()

    def update(self, id, title, author, year, isbn):
        """
            Updates a book from the book database
        """
        self.cursor.execute("UPDATE Book SET Title = ?, Author = ?, Year = ?, \
                            ISBN = ? WHERE Id = ?",
                            (title, author, year, isbn, id))
        self.connection.commit()

    def __del__(self):
        self.connection.close()
