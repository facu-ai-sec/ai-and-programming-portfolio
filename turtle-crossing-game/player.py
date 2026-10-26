from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.move_distance = 5
        self.penup()
        self.speed(10)
        self.goto(0, -280)
        self.shape("turtle")
        self.color("black")
        self.setheading(90)

    def movimiento(self):
        self.forward(MOVE_DISTANCE)

    def cambiar_nivel(self):
        self.goto(STARTING_POSITION)

    

        
