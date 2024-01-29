import time
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# WORK_MIN = 0.1
# SHORT_BREAK_MIN = 0.06
# LONG_BREAK_MIN = 0.1
POS = 0
TIMER = ""
INIT_TIMER = "00:00"


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global POS
    POS = 0

    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text=INIT_TIMER)
    head_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global POS
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    sessions = {"Work": [work_sec, GREEN, "Work"], "Short Break": [short_break_sec, PINK, "Break"],
                "Long Break": [long_break_sec, RED, "Break"]}

    session_orchestration = ["Work", "Short Break",
                             "Long Break"]

    if POS < len(session_orchestration):
        count = sessions[session_orchestration[POS]][0]
        color = sessions[session_orchestration[POS]][1]
        label = sessions[session_orchestration[POS]][2]
        head_label.config(text=label, fg=color)
        print(count, color, label)
        count_down(int(count))

        if label == "Work" and POS > 1:
            text = check_marks.cget("text") + "🚀"
            check_marks.config(text=text)
    else:
        window.after_cancel(TIMER)
    POS += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    canvas.itemconfig(timer_text, text=time.strftime('%M:%S', time.gmtime(count)))
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
head_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 34))
start_button = Button(text="ISS spotting", fg="blue", pady=2, highlightthickness=0, borderwidth=0, command=start_timer)
reset_button = Button(text="Reset", fg="blue", pady=2, highlightthickness=0, borderwidth=0, command=reset_timer)
check_marks = Label(bg=YELLOW, fg=GREEN)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text=INIT_TIMER, fill="white", font=(FONT_NAME, 35, "bold"))

head_label.grid(column=1, row=0)
canvas.grid(column=1, row=1)
start_button.grid(column=0, row=2)
check_marks.grid(column=1, row=3)
reset_button.grid(column=3, row=2)

window.mainloop()
