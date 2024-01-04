from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_direction = 1
        self.y_direction = 1
        self.move_speed = 0.1

    def move(self):
        # self.goto(self.xcor() + self.x_direction * 4 / 3, self.ycor() + self.y_direction * 1)
        new_x = self.xcor() + (self.x_direction * 10)
        new_y = self.ycor() + (self.y_direction * 10)
        self.goto(new_x, new_y)

        # ball is 20 x 20
        # screen is length x height = 800 x 600
        if self.ycor() >= 280:
            self.y_direction = -1
        elif self.ycor() <= - 280:
            self.y_direction = 1

    def bounce_from_paddle(self):
        self.x_direction = self.x_direction * -1
        self.move_speed *= 0.9

    def reset_game(self):
        self.goto(0, 0)
        self.x_direction = self.x_direction * -1
        self.move_speed = 0.1
