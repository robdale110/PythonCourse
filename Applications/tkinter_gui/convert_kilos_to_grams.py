"""
    kg to grams pounds and ounces converter
"""
from tkinter import *

def convert():
    """
        Convert an inputted amount of kg to grams, pounds and ounces
    """
    grams = float(kg_entered.get()) * 1000
    grams_text.insert(END, grams)
    pounds = float(kg_entered.get()) * 2.20462
    pounds_text.insert(END, pounds)
    ounces = float(kg_entered.get()) * 35.274
    ounces_text.insert(END, ounces)


window = Tk()

kg_label = Label(window, text="Kg")
kg_label.grid(row=0, column=0)
kg_entered = StringVar()
kg_entry = Entry(window, textvariable=kg_entered)
kg_entry.grid(row=0, column=1)
convert_button = Button(window, text="Convert", command=convert)
convert_button.grid(row=0, column=2)
grams_text = Text(window, height=1, width=20)
grams_text.grid(row=1, column=0)
pounds_text = Text(window, height=1, width=20)
pounds_text.grid(row=1, column=1)
ounces_text = Text(window, height=1, width=20)
ounces_text.grid(row=1, column=2)
window.mainloop()
