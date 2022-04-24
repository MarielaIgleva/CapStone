from turtle import Turtle
from random import randint


class Car:

    def __init__(self):
        self.start_x = 320
        self.cars = []

    def move_car(self):
        for car in self.cars:
            if car.xcor() > -320:
                new_x = car.xcor() - 10
                car.goto(new_x, car.ycor())

    def create_car(self):
        random_chance = randint(1,6)
        if random_chance == 1:
            car = Turtle()
            car.shape("square")
            car.shapesize(1, 2, 1)
            car.penup()
            car.color(randint(0, 120), randint(0, 120), randint(0, 120))
            random_y = randint(-240, 240)
            car.goto(self.start_x, random_y)
            self.cars.append(car)

