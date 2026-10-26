from turtle import Turtle
import random
import time

posibles_angulos = list(range(20, 70)) + list(range(110, 160)) + list(range(200, 250)) + list(range(290, 340))
angulo_inicial = random.choice(posibles_angulos)
class Pelota(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.setheading(angulo_inicial)

    def mover_pelota(self):
        self.forward(40)

    def cambiar_sentido_pared(self):
        new_angulo = (self.heading()) * -1
        self.setheading(new_angulo)

    def cambiar_sentido_jugadores(self):
      new_angulo = 180 - self.heading()
      self.setheading(new_angulo)
      self.forward(
          25
      )

    def reset_ball(self):
        self.goto(0, 0)
        time.sleep(3)
        self.setheading(random.choice(posibles_angulos))