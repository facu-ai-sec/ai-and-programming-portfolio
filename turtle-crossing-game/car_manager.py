from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5


class CarManager(Turtle):

  def __init__(self, position):
    super().__init__()
    self.move_distance = 5
    self.shape("square")
    self.shapesize(
        stretch_wid=1, stretch_len=2
    )  
    self.penup()
    self.color(random.choice(COLORS))
    
    self.goto(position)
    self.setheading(180)

  def move(self):
    
    self.forward(STARTING_MOVE_DISTANCE)
