from turtle import Turtle

class Jugador_1(Turtle):
    def __init__(self):
        super().__init__()

        self.goto(-450, 0)
        self.shape("square")
        self.shapesize(1, 5)
        self.color("white")
        self.setheading(90)
        self.penup()

    def arriba(self):
        if self.ycor() < 250:
            self.sety(self.ycor() + 100)

    def abajo(self):
        if self.ycor() > -250:
            self.sety(self.ycor() - 100)

    def ganador_j1(self):
        self.goto(0, 0)
        self.write(f"J1 WINS", move=True, align="center", font=('Courier', 15, 'normal'))

class Jugador_2(Turtle):
    def __init__(self):
        super().__init__()

        self.goto(450, 0)
        self.shape("square")
        self.shapesize(1, 5)
        self.color("white")
        self.setheading(90)
        self.penup()

    def arriba2(self):
        if self.ycor() < 250:
            self.sety(self.ycor() + 100)

    def abajo2(self):
        if self.ycor() > -250:
            self.sety(self.ycor() - 100)

    def ganador_j2(self):
        self.goto(0, 0)
        self.write(f"J2 WINS", move=True, align="center", font=('Courier', 15, 'normal'))