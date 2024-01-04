from time import sleep
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600, startx=0, starty=0)
screen.bgcolor("black")
screen.title("Ping-Pong")
screen.tracer(0)
scoreboard = Scoreboard()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.xcor() == 330 and ball.distance(r_paddle) < 50 or ball.xcor() == -330 and ball.distance(l_paddle) < 50:
        ball.bounce_from_paddle()

    if ball.xcor() >= 350:
        scoreboard.l_scores()
        ball.reset_game()

    if ball.xcor() < -350:
        scoreboard.r_scores()
        ball.reset_game()

screen.exitonclick()
