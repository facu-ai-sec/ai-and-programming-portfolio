from turtle import Screen
from jugadores import Jugador_1, Jugador_2
import time
from pelota import Pelota
from scoreboard import Scoreboard
from linea import Linea

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)

facu = Jugador_1()
juan = Jugador_2()
pelota = Pelota()
scoreboard = Scoreboard()
linea = Linea()

screen.listen()
screen.onkey(fun=facu.arriba, key="w")
screen.onkey(fun=facu.abajo, key="s")
screen.onkey(fun=juan.arriba2, key="Up")
screen.onkey(fun=juan.abajo2, key="Down")

game_is_on = True
puntaje1 = 0
puntaje2 = 0

while game_is_on:
    screen.update()
    pelota.mover_pelota()

    if pelota.distance(facu) < 50 or pelota.distance(juan) < 50:
        pelota.cambiar_sentido_jugadores()

    if pelota.ycor() > 270 or pelota.ycor() < -270:
        pelota.cambiar_sentido_pared()

    if pelota.xcor() > 700:
        puntaje1 += 1

        if puntaje1 >= 3:
            facu.ganador_j1()
            game_is_on = False

        scoreboard.update_scoreboard(puntaje1, puntaje2)
        pelota.reset_ball()
    elif pelota.xcor() < -700:
        puntaje2 += 1

        if puntaje2 >= 3:
            juan.ganador_j2()
            game_is_on = False
        scoreboard.update_scoreboard(puntaje1, puntaje2)
        pelota.reset_ball()

    





    time.sleep(0.1)

screen.exitonclick()