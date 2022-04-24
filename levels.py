from turtle import Turtle

ALIGNMENT = "center"
FONT_STYLE = ('Courier', 20, 'italic')


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level_on = 1
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)
        self.write(f"Level: {self.level_on}", align=ALIGNMENT, font=FONT_STYLE)

    def new_level(self):
        self.clear()
        self.level_on += 1
        self.write(f"Level: {self.level_on}", align=ALIGNMENT, font=FONT_STYLE)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over!", align=ALIGNMENT, font=FONT_STYLE)
