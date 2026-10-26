import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

CARRILES = [
    30,
    70,
    110,
    150,
    190,
    230,
    270,
    -230,
    -190,
    -150,
    -110,
    -70,
    -30,
    10,
    50,
    90,
    130,
]

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()
player = Player()
screen.listen()
screen.onkey(player.movimiento, "Up")

contador = 0
cars_list = []
game_is_on = True

while game_is_on:
  screen.update()
  scoreboard.actual_scoreboard(contador)
  time.sleep(0.1)

 
  if random.randint(1, 4) == 1:
    random_y = random.choice(CARRILES)
    new_car = CarManager((290, random_y))

    cars_list.append(new_car)

  for car in cars_list:


    car.move()
    if car.distance(player) < 30:
      scoreboard.game_over()
      scoreboard.clear()
      game_is_on = False
    if car.xcor() < -320:
      car.hideturtle()
      cars_list.remove(car)

  

  if player.distance(0, 280) < 5:
    contador += 1
    scoreboard.actual_scoreboard(contador)
    car.move_distance += 20


    player.goto(0, -280)

  
print(cars_list)

screen.exitonclick()