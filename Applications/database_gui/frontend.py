"""
    A program that stores book information:
    Title, Author, Year, ISBN

    User can:
    View all of the records
    Search for an entry
    Add an entry
    Update an entry
    Delete an entry
    Close the application
"""
from tkinter import *
import backend

def set_up_interface():
    """
        Set up the grid interface
    """
    title_label = Label(window, text="Title")
    title_label.grid(row=0, column=0)
    author_label = Label(window, text="Author")
    author_label.grid(row=0, column=2)
    year_label = Label(window, text="Year")
    year_label.grid(row=1, column=0)
    isbn_label = Label(window, text="ISBN")
    isbn_label.grid(row=1, column=2)

    title = StringVar()
    title_entry = Entry(window, textvariable=title)
    title_entry.grid(row=0, column=1)
    author = StringVar()
    author_entry = Entry(window, textvariable=author)
    author_entry.grid(row=0, column=3)
    year = StringVar()
    year_entry = Entry(window, textvariable=year)
    year_entry.grid(row=1, column=1)
    isbn = StringVar()
    isbn_entry = Entry(window, textvariable=isbn)
    isbn_entry.grid(row=1, column=3)

    book_list = Listbox(window, height=6, width=35)
    book_list.grid(row=2, column=0, rowspan=6, columnspan=2)

    book_scrollbar = Scrollbar(window)
    book_scrollbar.grid(row=2, column=2, rowspan=6)

    book_list.configure(yscrollcommand=book_scrollbar.set)
    book_scrollbar.configure(command=book_list.yview)

    viewall_button = Button(window, text="View All", width=12)
    viewall_button.grid(row=2, column=3)
    searchentry_button = Button(window, text="Search Entry", width=12)
    searchentry_button.grid(row=3, column=3)
    addentry_button = Button(window, text="Add Entry", width=12)
    addentry_button.grid(row=4, column=3)
    update_button = Button(window, text="Update", width=12)
    update_button.grid(row=5, column=3)
    delete_button = Button(window, text="Delete", width=12)
    delete_button.grid(row=6, column=3)
    close_button = Button(window, text="Close", width=12)
    close_button.grid(row=7, column=3)

window = Tk()
set_up_interface()
window.mainloop()
