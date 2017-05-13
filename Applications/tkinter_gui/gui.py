from tkinter import *

window = Tk()

first_button = Button(window, text="Execute")
first_button.grid(row=0, column=0)
first_entry = Entry(window)
first_entry.grid(row=0, column=1)
first_text = Text(window, height=1, width=20)
first_text.grid(row=0, column=2)
window.mainloop()