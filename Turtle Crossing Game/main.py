from turtle import Screen
import time
from player import Player

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Raymond's Turtle Crossing Game")
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

screen.exitonclick()
