from turtle import Turtle

MOVEMENT_SPEED = 45


class Bumper(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=8)
        self.penup()
        self.goto(0, -205)
        self.showturtle()

    def right(self):
        new_right = self.xcor() + MOVEMENT_SPEED
        self.goto(new_right, self.ycor())

    def left(self):
        new_left = self.xcor() - MOVEMENT_SPEED
        self.goto(new_left, self.ycor())

    def bumper_reset(self):
        self.goto(0, -205)
