from turtle import Turtle

X_COORDINATES = 0


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.goto(x=X_COORDINATES, y=-280)

    def move_up(self):
        new_y = self.ycor() + 10
        self.goto(x=X_COORDINATES, y=new_y)

    def reset(self):
        self.goto(x=X_COORDINATES, y=-280)


