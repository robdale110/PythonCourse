from tkinter import *

window = Tk()

def km_to_miles():
    print(entry_value.get())
    miles = float(entry_value.get()) * 1.6
    first_text.insert(END, miles)

first_button = Button(window, text="Execute", command=km_to_miles)
first_button.grid(row=0, column=0)
entry_value = StringVar()
first_entry = Entry(window, textvariable=entry_value)
first_entry.grid(row=0, column=1)
first_text = Text(window, height=1, width=20)
first_text.grid(row=0, column=2)
window.mainloop()