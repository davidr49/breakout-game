from turtle import Turtle
import random

block_positions = []
y_cor = 200
x_cor = -380

for n in range(4):
    for n in range(11):
        block_positions.append((x_cor, y_cor))
        x_cor += 75
    y_cor -= 50
    x_cor = -380

color_list = ['blue', 'green', 'yellow', 'gold', 'red', 'purple', 'silver', 'orange', 'maroon','violet','magenta','navy',
              'skyblue','cyan','turquoise','lightgreen','green','darkgreen', 'chocolate','brown','gray']


class Block(Turtle):

    def __init__(self):
        super().__init__()
        self.block_list = []
        self.start_block()
        self.level_over = False

    def start_block(self):
        for position in block_positions:
            self.add_blocks(position)

    def add_blocks(self, position):
        new_block = Turtle('square')
        new_block.penup()
        new_block.speed('fastest')
        new_block.color(random.choice(color_list))
        new_block.shapesize(stretch_wid=1, stretch_len=3)
        new_block.showturtle()
        new_block.goto(position)
        self.block_list.append(new_block)

    def reset_blocks(self):
        global block_positions
        self.block_list.clear()
        block_positions.clear()
        y_cor = 200
        x_cor = -400
        for n in range(4):
            for n in range(11):
                block_positions.append((x_cor, y_cor))
                x_cor += 75
            y_cor -= 50
            x_cor = -400
        self.start_block()

    def check_blocks(self):
        for blocks in self.block_list:
            if self.block_list.count(blocks) < 1:
                self.level_over = True
