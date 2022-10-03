from turtle import Turtle

FONT = ('Arial', 15, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.total_score = 0
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(-250, -280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.total_score}                          High Score: {self.high_score}', align='center', font=FONT)

    def add_point(self):
        self.clear()
        self.total_score += 1
        self.update_scoreboard()

    def reset_scoreboard(self):
        if self.total_score > self.high_score:
            self.high_score= self.total_score
            with open('data.txt', mode='w') as data:
                data.write(f'{self.high_score}')
        self.total_score = 0
        self.update_scoreboard()