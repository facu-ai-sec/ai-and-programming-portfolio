from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.write("J1 Score: 0           J2 Score: 0", move=False, align="center", font=('Courier', 15, 'normal'))

    def update_scoreboard(self, pu1, pu2):
        self.clear()
        self.goto(0, 260)
        self.write(f"J1 Score: {pu1}           J2 Score: {pu2}", move=False, align="center", font=('Courier', 15, 'normal'))