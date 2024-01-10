from tkinter import *

window = Tk()
window.title("GUI Program")
window.minsize(500, 300)
window.config(padx=20, pady=20)
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label["text"] = "Not a label"
my_label.config(text="Well yes a label")


def button_clicked():
    my_label["text"] = entry.get()


button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)
button_1 = Button(text="Click me too", command=button_clicked)
button_1.grid(column=3, row=0)

entry = Entry(width=10)
entry.grid(column=4, row=4)


def calculate(n, **kwargs):
    # kwargs is a dict
    sum = n + kwargs.get("add")
    mul = n * kwargs.get("mul")

    return sum, mul


print(calculate(9, add=10, mul=8))


def add(*args):
    # args is a tuple
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(2, 3, 4, 5, 6, 7, 8, 9))

window.mainloop()
