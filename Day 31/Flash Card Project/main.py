from tkinter import *

import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
SHOW_ENG_WORD = ''
CURRENT_WORD = pd.Series
WORDS_LEARNED_DF = pd.DataFrame(columns=["Dutch", "English"])
WORDS_LEARNED = []


def get_new_word():
    words = pd.read_csv("./data/dutch_words.csv")
    try:
        words_learned = pd.read_csv("./data/words_learned.csv")
    except FileNotFoundError:
        WORDS_LEARNED_DF.to_csv("./data/words_learned.csv", index=False)
        words_to_learn = words
    else:
        words_to_learn = pd.concat([words, words_learned]).drop_duplicates(keep=False)

    new_word = words_to_learn.sample(n=1).iloc[0]
    return new_word


def show_english_translation_of_dutch_word(word):
    canvas.itemconfig(image_on_canvas, image=card_back_image)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=word["English"], fill="white")


def show_next_card():
    global SHOW_ENG_WORD, CURRENT_WORD
    CURRENT_WORD = get_new_word()
    canvas.itemconfig(image_on_canvas, image=card_front_image)
    canvas.itemconfig(language_text, text="Dutch", fill="black")
    canvas.itemconfig(word_text, text=CURRENT_WORD["Dutch"], fill="black")
    SHOW_ENG_WORD = window.after(3000, show_english_translation_of_dutch_word, CURRENT_WORD)


def right_button_click():
    window.after_cancel(SHOW_ENG_WORD)
    with open("./data/words_learned.csv", mode="a") as words_learned:
        words_learned.write(f"{CURRENT_WORD["Dutch"]},{CURRENT_WORD["English"]}\n")
    show_next_card()


def wrong_button_click():
    window.after_cancel(SHOW_ENG_WORD)
    show_next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
card_back_image = PhotoImage(file="./images/card_back.png")
card_front_image = PhotoImage(file="./images/card_front.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image_on_canvas = canvas.create_image(400, 526 / 2, image=card_front_image)
language_text = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)
right_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")
right_button = Button(image=right_image, highlightthickness=0, bd=0, command=right_button_click)
right_button.grid(row=1, column=1)

wrong_button = Button(image=wrong_image, highlightthickness=0, bd=0, command=wrong_button_click)
wrong_button.grid(row=1, column=0)

show_next_card()

window.mainloop()
