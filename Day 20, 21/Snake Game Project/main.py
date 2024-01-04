from time import sleep
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=1000, height=1000)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

new_snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(new_snake.up, "Up")
screen.onkey(new_snake.down, "Down")
screen.onkey(new_snake.left, "Left")
screen.onkey(new_snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    sleep(0.05)
    new_snake.move()

    if new_snake.head.distance(food) < 15:
        food.refresh()
        new_snake.extend()
        scoreboard.increase_score_by_one()

    # Detect collision with wall
    if new_snake.head.xcor() > 480 or new_snake.head.xcor() < -480 or new_snake.head.ycor() > 480 or new_snake.head.xcor() < -480:
        game_is_on = False
        scoreboard.game_over()
    # Detect collision with tail

    for segment in new_snake.segments[1:]:
        if new_snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
# segment(start:end:increment)
# increment can be negative for reversing the list
screen.exitonclick()
