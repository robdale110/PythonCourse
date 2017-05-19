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
from backend import Database

class FrontEnd(object):
    """
        Class for creating the gui
    """
    def __init__(self):
        self.database = Database("books.db")
        self.window = Tk()
        self.window.wm_title("Book Store")

        self.title_label = Label(self.window, text="Title")
        self.title_label.grid(row=0, column=0)
        self.author_label = Label(self.window, text="Author")
        self.author_label.grid(row=0, column=2)
        self.year_label = Label(self.window, text="Year")
        self.year_label.grid(row=1, column=0)
        self.isbn_label = Label(self.window, text="ISBN")
        self.isbn_label.grid(row=1, column=2)

        self.title = StringVar()
        self.title_entry = Entry(self.window, textvariable=self.title)
        self.title_entry.grid(row=0, column=1)
        self.author = StringVar()
        self.author_entry = Entry(self.window, textvariable=self.author)
        self.author_entry.grid(row=0, column=3)
        self.year = StringVar()
        self.year_entry = Entry(self.window, textvariable=self.year)
        self.year_entry.grid(row=1, column=1)
        self.isbn = StringVar()
        self.isbn_entry = Entry(self.window, textvariable=self.isbn)
        self.isbn_entry.grid(row=1, column=3)

        self.book_list = Listbox(self.window, height=6, width=35)
        self.book_list.grid(row=2, column=0, rowspan=6, columnspan=2)
        self.book_list.bind("<<ListboxSelect>>", self.get_selected_row)

        self.book_scrollbar = Scrollbar(self.window)
        self.book_scrollbar.grid(row=2, column=2, rowspan=6)

        self.book_list.configure(yscrollcommand=self.book_scrollbar.set)
        self.book_scrollbar.configure(command=self.book_list.yview)

        viewall_button = Button(self.window, text="View All", width=12, command=self.view_command)
        viewall_button.grid(row=2, column=3)
        searchentry_button = Button(self.window, text="Search Entry", width=12, command=self.search_command)
        searchentry_button.grid(row=3, column=3)
        addentry_button = Button(self.window, text="Add Entry", width=12, command=self.insert_command)
        addentry_button.grid(row=4, column=3)
        update_button = Button(self.window, text="Update", width=12, command=self.update_command)
        update_button.grid(row=5, column=3)
        delete_button = Button(self.window, text="Delete", width=12, command=self.delete_command)
        delete_button.grid(row=6, column=3)
        close_button = Button(self.window, text="Close", width=12, command=self.window.destroy)
        close_button.grid(row=7, column=3)

        self.window.mainloop()

    def view_command(self):
        """
            Call the view method on the backend and put the results in the
            Listbox
        """
        self.book_list.delete(0, END)

        for row in self.database.view():
            self.book_list.insert(END, row)

    def search_command(self):
        """
            Call the search method on the backend, passing the values
            entered in the text boxes
        """
        self.book_list.delete(0, END)

        for row in self.database.search(self.title.get(), self.author.get(), self.year.get(), self.isbn.get()):
            self.book_list.insert(END, row)

    def insert_command(self):
        """
            Call the insert method on the back end passing the values entered
        """
        self.database.insert_book(self.title.get(), self.author.get(), self.year.get(), self.isbn.get())
        self.book_list.delete(0, END)
        self.book_list.insert(END, (self.title.get(), self.author.get(), self.year.get(), self.isbn.get()))

    def get_selected_row(self, event):
        """
            Gets the selected row in the listbox
        """
        global selected_tuple
        index = self.book_list.curselection()[0]
        selected_tuple = self.book_list.get(index)
        self.title_entry.delete(0, END)
        self.title_entry.insert(END, selected_tuple[1])
        self.author_entry.delete(0, END)
        self.author_entry.insert(END, selected_tuple[2])
        self.year_entry.delete(0, END)
        self.year_entry.insert(END, selected_tuple[3])
        self.isbn_entry.delete(0, END)
        self.isbn_entry.insert(END, selected_tuple[4])
        return selected_tuple

    def delete_command(self):
        """
            Deletes an entry from the book database
        """
        self.database.delete(selected_tuple[0])

    def update_command(self):
        """
            Updates a selected entry
        """
        self.database.update(selected_tuple[0], self.title.get(), self.author.get(),
                             self.year.get(), self.isbn.get())

front_end = FrontEnd()
