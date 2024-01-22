from random import randint, shuffle, choice
from tkinter import *
from tkinter import messagebox
import pyperclip
FONT_NAME = "Ariel"
FONT_SIZE = 14
STANDARD_BG = "white"
STANDARD_FG = "black"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generatePassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letter + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    # password = ""
    # for char in password_list:
    #     password += char

    # print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    entry = website_entry.get() + ' | ' + email_username_entry.get() + ' | ' + password_entry.get()
    if len(website_entry.get()) == 0 or len(email_username_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showerror(title="Oops", message="Some fields are empty")
    else:
        okay = messagebox.askokcancel(title=website_entry.get(), message="Is it Ok to save?")
        if okay:
            with open(f"./data.txt", mode="a") as data:
                data.write(f"{entry}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=STANDARD_BG)
canvas = Canvas(width=200, height=200, highlightthickness=0, bg=STANDARD_BG)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_img)

# labels
website_label = Label(text="Website:", font=(FONT_NAME, FONT_SIZE), bg=STANDARD_BG, fg=STANDARD_FG)
email_username_label = Label(text="Email/Username:", font=(FONT_NAME, FONT_SIZE), bg=STANDARD_BG, fg=STANDARD_FG)
password_label = Label(text="Password:", font=(FONT_NAME, FONT_SIZE), bg=STANDARD_BG, fg=STANDARD_FG)

# entry
website_entry = Entry(width=35, bg=STANDARD_BG, fg=STANDARD_FG, justify="left")
website_entry.focus()
email_username_entry = Entry(width=35, bg=STANDARD_BG, fg=STANDARD_FG)
email_username_entry.insert(0, "abc@gmail.com")
password_entry = Entry(width=21, bg=STANDARD_BG, fg=STANDARD_FG)

# button
generate_password_button = Button(command=generatePassword, text="Generate Password", pady=2, highlightthickness=0,
                                  borderwidth=0, bg=STANDARD_BG,
                                  fg=STANDARD_FG)
add_button = Button(command=save, text="Add", pady=2, highlightthickness=0, borderwidth=0, width=36, bg=STANDARD_BG,
                    fg=STANDARD_FG)

# alignment on canvas
website_label.grid(column=0, row=1)
email_username_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

canvas.grid(column=1, row=0)
website_entry.grid(column=1, row=1, columnspan=2)
email_username_entry.grid(column=1, row=2, columnspan=2)
password_entry.grid(column=1, row=3)
add_button.grid(column=1, row=4, columnspan=2)

generate_password_button.grid(column=2, row=3)

window.mainloop()
