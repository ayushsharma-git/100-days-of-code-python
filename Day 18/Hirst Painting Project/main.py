import random
import turtle as t
from turtle import Turtle, Screen
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     rgb_tuple = (color.rgb.r, color.rgb.g, color.rgb.b)
#     rgb_colors.append(rgb_tuple)
#
# print(rgb_colors)

color_list = [(152, 72, 58), (41, 126, 82), (241, 223, 195), (197, 151, 119), (154, 59, 78), (13, 19, 41), (107, 172, 213), (115, 184, 151), (39, 14, 24), (43, 16, 10), (43, 107, 147), (199, 235, 215), (56, 171, 128), (234, 211, 101), (152, 27, 42), (208, 68, 81), (9, 40, 20), (242, 215, 226), (151, 29, 21), (195, 221, 238), (202, 83, 75), (198, 135, 156), (11, 101, 54), (134, 223, 185), (31, 36, 153), (46, 161, 187), (84, 111, 199), (248, 163, 152), (166, 151, 58), (134, 215, 231)]
tim = Turtle()
tim.speed(0)
tim.shape("circle")
t.colormode(255)
for y in range(10):
    tim.teleport(-150, -150 + y*50)
    for _ in range(10):
        tim.pendown()
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)
tim.hideturtle()
screen = Screen()
screen.exitonclick()
