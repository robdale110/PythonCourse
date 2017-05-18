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

def view_command():
    """
        Call the view method on the backend and put the results in the
        Listbox
    """
    book_list.delete(0, END)

    for row in backend.view():
        book_list.insert(END, row)

def search_command():
    """
        Call the search method on the backend, passing the values
        entered in the text boxes
    """
    book_list.delete(0, END)

    for row in backend.search(title.get(), author.get(), year.get(), isbn.get()):
        book_list.insert(END, row)

def insert_command():
    """
        Call the insert method on the back end passing the values entered
    """
    backend.insert_book(title.get(), author.get(), year.get(), isbn.get())
    book_list.delete(0, END)
    book_list.insert(END, (title.get(), author.get(), year.get(), isbn.get()))

def get_selected_row(event):
    """
        Gets the selected row in the listbox
    """
    global selected_tuple
    index = book_list.curselection()[0]
    selected_tuple = book_list.get(index)
    title_entry.delete(0, END)
    title_entry.insert(END, selected_tuple[1])
    author_entry.delete(0, END)
    author_entry.insert(END, selected_tuple[2])
    year_entry.delete(0, END)
    year_entry.insert(END, selected_tuple[3])
    isbn_entry.delete(0, END)
    isbn_entry.insert(END, selected_tuple[4])
    return selected_tuple

def delete_command():
    """
        Deletes an entry from the book database
    """
    backend.delete(selected_tuple[0])

def update_command():
    """
        Updates a selected entry
    """
    backend.update(selected_tuple[0], title.get(), author.get(), year.get(), isbn.get())

window = Tk()
window.wm_title("Book Store")

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
book_list.bind("<<ListboxSelect>>", get_selected_row)

book_scrollbar = Scrollbar(window)
book_scrollbar.grid(row=2, column=2, rowspan=6)

book_list.configure(yscrollcommand=book_scrollbar.set)
book_scrollbar.configure(command=book_list.yview)

viewall_button = Button(window, text="View All", width=12, command=view_command)
viewall_button.grid(row=2, column=3)
searchentry_button = Button(window, text="Search Entry", width=12, command=search_command)
searchentry_button.grid(row=3, column=3)
addentry_button = Button(window, text="Add Entry", width=12, command=insert_command)
addentry_button.grid(row=4, column=3)
update_button = Button(window, text="Update", width=12, command=update_command)
update_button.grid(row=5, column=3)
delete_button = Button(window, text="Delete", width=12, command=delete_command)
delete_button.grid(row=6, column=3)
close_button = Button(window, text="Close", width=12, command=window.destroy)
close_button.grid(row=7, column=3)

window.mainloop()
