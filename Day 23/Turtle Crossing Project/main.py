import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.move_cars(scoreboard.level)
    screen.update()

    if player.if_over_finish_line():
        scoreboard.level += 1
        scoreboard.print_scorecard()

    if car_manager.if_player_collided_with_any_car(player):
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
