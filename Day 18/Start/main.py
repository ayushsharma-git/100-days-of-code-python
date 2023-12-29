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
#         tim.color("black")
#         tim.forward(10)
#         tim.color("white")
#         tim.forward(10)
#     tim.right(90)
#     tim.color("black")

# for _ in range(40):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)


# for sides in range(3,11):
#     tim.pencolor(random.randint(0,255), random.randint(0,255), random.randint(0,255) )
#     for _ in range(sides):
#         tim.forward(100)
#         tim.right(360/sides)

# for _ in range(2000):
#     tim.pencolor(random.randint(0,255), random.randint(0,255), random.randint(0,255) )
#     tim.forward(10)
#     tim.setheading(random.choice([0,90,180,270]))


def draw_spirograph(size_of_gap):
    for tilt in range(int(360 / size_of_gap)):
        tim.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        tim.circle(80)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(10)

screen = Screen()
screen.colormode(255)
screen.exitonclick()
