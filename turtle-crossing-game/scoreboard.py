from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)

    def actual_scoreboard(self, score):
        self.clear()
        self.write(f"SCORE: {score}", align="center", font=("Courier", 15, "normal"))

    def game_over(self):
        game_over_turtle = Turtle()
        game_over_turtle.hideturtle()
        game_over_turtle.penup()
        game_over_turtle.color("black")
        game_over_turtle.goto(0, 0)
        game_over_turtle.write("GAME OVER", align="center", font=('Courier', 24, 'normal'))