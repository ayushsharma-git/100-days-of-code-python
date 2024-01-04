from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 80, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.print_scorecard()

    def print_scorecard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, move=False, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, move=False, align=ALIGNMENT, font=FONT)

    def l_scores(self):
        self.l_score += 1
        self.print_scorecard()

    def r_scores(self):
        self.r_score += 1
        self.print_scorecard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)
