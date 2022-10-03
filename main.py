from turtle import Screen
from bumper import Bumper
from block import Block
from ball import Ball
from scoreboard import Scoreboard
import time

#end game, reset functions needed



screen = Screen()
screen.setup(width=900, height=600)
screen.title('Breakout')
screen.bgcolor('black')
screen.listen()
screen.tracer(0)

bumper = Bumper()
block = Block()
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(bumper.left, 'Left')
screen.onkey(bumper.right, 'Right')

screen.update()
time.sleep(1)

game_on = True
while game_on:
    screen.update()
    ball.move()

    if ball.distance(bumper) < 90 and ball.ycor() < -190:
        ball.bounce()

    if ball.ycor() > 250:
        ball.bounce()

    if ball.xcor() < -430 or ball.xcor() > 430:
        ball.wall_bounce()

    if ball.ycor() < -210:
        ball.ball_reset()
        screen.update()
        time.sleep(1)

    for blocks in block.block_list:
        if blocks.distance(ball) < 30:
            block.block_list.remove(blocks)
            blocks.hideturtle()
            blocks.clear()
            scoreboard.add_point()
            ball.bounce()

    # if block.block_list.count() < 1:


screen.exitonclick()
