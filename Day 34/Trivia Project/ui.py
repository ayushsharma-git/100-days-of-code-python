from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)
        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.question = self.canvas.create_text(150, 125, text="Test", fill=THEME_COLOR, font=("Arial", 20, "italic"),
                                                width=280)

        true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_btn_click)
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_btn_click)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.question, text="You have reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_btn_click(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_btn_click(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, func=self.get_next_question)
