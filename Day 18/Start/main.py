import turtle
from turtle import Turtle, Screen
import random

# from turtle import *

tim = Turtle()
tim.color("medium slate blue")
tim.shape("circle")
tim.speed(0)
tim.pensize(0)
turtle.colormode(255)


# for _ in range(4):
#     for _ in range(10):
#         tim_color.color("black")
#         tim_color.forward(10)
#         tim_color.color("white")
#         tim_color.forward(10)
#     tim_color.right(90)
#     tim_color.color("black")

# for _ in range(40):
#     tim_color.pendown()
#     tim_color.forward(10)
#     tim_color.penup()
#     tim_color.forward(10)


# for sides in range(3,11):
#     tim_color.pencolor(random.randint(0,255), random.randint(0,255), random.randint(0,255) )
#     for _ in range(sides):
#         tim_color.forward(100)
#         tim_color.right(360/sides)

# for _ in range(2000):
#     tim_color.pencolor(random.randint(0,255), random.randint(0,255), random.randint(0,255) )
#     tim_color.forward(10)
#     tim_color.setheading(random.choice([0,90,180,270]))


def draw_spirograph(size_of_gap):
    for tilt in range(int(360 / size_of_gap)):
        tim.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        tim.circle(80)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(10)

screen = Screen()
screen.colormode(255)
screen.exitonclick()
