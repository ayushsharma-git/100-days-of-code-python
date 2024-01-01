from time import sleep
from turtle import Screen

from snake import Snake

screen = Screen()
screen.setup(width=1000, height=1000)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

new_snake = Snake()
screen.listen()

screen.onkey(new_snake.up, "Up")
screen.onkey(new_snake.down, "Down")
screen.onkey(new_snake.left, "Left")
screen.onkey(new_snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    sleep(0.1)
    new_snake.move()
screen.exitonclick()
