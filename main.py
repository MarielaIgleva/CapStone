from turtle import Screen
from player import Player
from cars import Car
from levels import Level
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.colormode(255)

player = Player()
car = Car()
level = Level()

screen.onkeypress(key="Up", fun=player.move_up)
screen.listen()

game_on = True
time_sleep = 0.1
while game_on:

    time.sleep(time_sleep)
    car.create_car()
    car.move_car()
    screen.update()

    for vehicle in car.cars:
        if player.distance(vehicle) < 20:
            game_on = False
            level.game_over()

    if player.ycor() > 270:
        time_sleep -= 0.01
        level.new_level()
        player.reset()

screen.exitonclick()
