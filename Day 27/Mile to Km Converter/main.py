from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(500, 300)
window.config(padx=20, pady=20)

mile_entry = Entry()
is_equal_to_label = Label(text="is equal to")
mile_label = Label(text="Miles")
km_label = Label(text="Km")
button = Button(text="Calculate")

mile_entry.grid(column=1, row= 0)
is_equal_to_label.grid(column=0, row= 2)
mile_label.grid(column=2, row= 0)
mile_label.grid(column=2, row= 0)




