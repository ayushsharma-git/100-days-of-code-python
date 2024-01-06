from turtle import Turtle

FONT = ("Courier", 24, "normal")
GAME_OVER_ALIGNMENT = 'center'
LEVEL_ALIGNMENT = 'left'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.level = 1
        self.print_scorecard()

    def print_scorecard(self):
        self.clear()
        self.goto(-295, 275)
        self.write(f"Level: {self.level}", move=False, align=LEVEL_ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=GAME_OVER_ALIGNMENT, font=FONT)
