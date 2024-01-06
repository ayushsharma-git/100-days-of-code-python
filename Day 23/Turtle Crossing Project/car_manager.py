import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
NUM_CARS = 25


class CarManager:
    def __init__(self):
        self.cars = []
        self.create_cars()
        self.move_cars(1)

    def create_cars(self):
        for _ in range(NUM_CARS):
            car = Turtle(shape="square")
            car.shapesize(stretch_wid=1, stretch_len=3)
            car.penup()
            car.color(random.choice(COLORS))
            car.goto(random.randint(-300, 300), random.randint(-250, 260))
            self.cars.append(car)

    def move_cars(self, level):
        multiplier = level - 1
        move_by = STARTING_MOVE_DISTANCE + multiplier * MOVE_INCREMENT
        for car in self.cars:
            car.goto(car.xcor() - move_by, car.ycor())
            if car.xcor() < -300:
                car.goto(300, car.ycor())

    def if_player_collided_with_any_car(self, player):
        for car in self.cars:
            if 40 >= car.xcor() >= -40:
                y_diff = abs(player.ycor() - car.ycor())
                if y_diff < 20:
                    # print( f"x {car.xcor()},/n y {car.ycor()},/n dist {car.distance(player)},/n player x {
                    # player.xcor()},/n player y {player.ycor()}")
                    return True
