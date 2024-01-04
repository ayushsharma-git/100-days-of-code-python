from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 470)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(f"Score = {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score_by_one(self):
        self.clear()
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)
