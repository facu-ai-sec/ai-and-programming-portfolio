from turtle import Turtle

class Linea(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.goto(0, -300)
        self.setheading(90)
        self.forward(560)
