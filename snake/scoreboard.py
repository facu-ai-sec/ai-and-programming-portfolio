from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", move=True, align="center", font=('Courier', 15, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=True, align="center", font=('Courier', 15, 'normal'))
        