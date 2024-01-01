from turtle import Turtle, Screen
import random
# turtle dimensions are 40x40
colors = ["red", "pink", "blue", "black", "green", "orange"]
is_race_on = False
screen = Screen()
screen.setup(width=1000,height=1000)
user_bet = screen.textinput(title="Place your bet", prompt=f"Which turtle will win the race {colors}?\nEnter a color:")
turtles = {}
y = 150
for color in colors:
    turtles[color] = Turtle(shape="turtle")
    turtles[color].color(color)
    turtles[color].penup()
    turtles[color].teleport(x=-480, y=y)
    y -= 60

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle_color in turtles:
        turtle_boi = turtles[turtle_color]
        turtle_boi.forward(random.randint(0,10))
        if turtle_boi.xcor() > 470:
            is_race_on = False
            winner = turtle_color

if user_bet == winner:
    print(f"You win!")
else:
    print(f"You lost!")
print(f"The winner is {winner} turtle")





screen.listen()
screen.exitonclick()




#
# def move_forward():
#     tim_color.forward(10)
# def move_backwards():
#     tim_color.backward(10)
#
# def turn_clockwise():
#     # tim_color.left(90)
#     # tim_color.heading()
#     # tim_color.forward(10)
#     new_heading = tim_color.heading() + 10
#     tim_color.setheading(new_heading)
# def turn_counter_clockwise():
#     # tim_color.right(90)
#     # tim_color.heading()
#     # tim_color.forward(10)
#     new_heading = tim_color.heading() - 10
#     tim_color.setheading(new_heading)
# def clear_screen():
#     tim_color.reset()
#
# screen.onkey(fun= move_forward, key="w")
# screen.onkey(fun= move_backwards, key="s")
# screen.onkey(fun= turn_clockwise, key="a")
# screen.onkey(fun= turn_counter_clockwise, key="d")
# screen.onkey(fun= clear_screen, key="c")