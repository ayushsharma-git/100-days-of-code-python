from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(50, 30)
window.config(padx=20, pady=20)


def calculate():
    in_km = round(float(mile_entry.get()) * 1.609, ndigits=2)
    in_km_label.config(text=in_km)


mile_entry = Entry(width=3)
is_equal_to_label = Label(text="is equal to")
mile_label = Label(text="Miles")
km_label = Label(text="Km")
in_km_label = Label(text=0)
button = Button(text="Calculate", command=calculate)

mile_entry.grid(column=1, row=0)
is_equal_to_label.grid(column=0, row=1)
mile_label.grid(column=2, row=0)
km_label.grid(column=2, row=1)
in_km_label.grid(column=1, row=1)
button.grid(column=1, row=2)

window.mainloop()
