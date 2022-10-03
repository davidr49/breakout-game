from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.startpos = random.randint(-400, 400)
        self.goto(self.startpos, 0)
        self.x_move=-4.5
        self.y_move=-4.5


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def wall_bounce(self):
        self.x_move *= -1

    def ball_reset(self):
        self.goto(self.startpos, 0)