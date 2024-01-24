import random
from tkinter import *

import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"


def get_new_word():
    words = pd.read_csv("./data/dutch_words.csv")
    new_word = words.loc[random.randint(0, 499)]
    return new_word


def right_button_click():
    new_word = get_new_word()
    canvas.itemconfig(language_text, text="Dutch")
    canvas.itemconfig(word_text, text=new_word["Dutch"])


def wrong_button_click():
    right_button_click()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
card_back_image = PhotoImage(file="./images/card_back.png")
card_front_image = PhotoImage(file="./images/card_front.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 526 / 2, image=card_front_image)
language_text = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)
right_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")
right_button = Button(image=right_image, highlightthickness=0, bd=0, command=right_button_click)
right_button.grid(row=1, column=1)

wrong_button = Button(image=wrong_image, highlightthickness=0, bd=0, command=wrong_button_click)
wrong_button.grid(row=1, column=0)

right_button_click()

window.mainloop()
