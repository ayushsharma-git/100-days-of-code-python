from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.move_to_starting_position()

    def move_to_starting_position(self):
        self.goto(STARTING_POSITION)

    def move(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def if_over_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            self.move_to_starting_position()
            return True
