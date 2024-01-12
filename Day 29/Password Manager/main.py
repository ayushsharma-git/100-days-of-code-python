from tkinter import *

FONT_NAME = "Ariel"
FONT_SIZE = 14
STANDARD_BG = "white"
STANDARD_FG = "black"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
website_entry = Entry(width=35, bg=STANDARD_BG, borderwidth=0.01)
email_username_entry = Entry(width=35, bg=STANDARD_BG)
password_entry = Entry(width=21, bg=STANDARD_BG,borderwidth=0)

# button
generate_password_button = Button(text="Generate Password", pady=2, highlightthickness=0, borderwidth=0, bg=STANDARD_BG,
                                  fg=STANDARD_FG)
add_button = Button(text="Add", pady=2, highlightthickness=0, borderwidth=0, width=36, bg=STANDARD_BG, fg=STANDARD_FG)

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
