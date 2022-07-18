from turtle import Screen as s, Turtle as t
import turtle

timmy_the_turtle = t()

timmy_the_turtle.pen(fillcolor="black", pencolor="red", pensize=5)

for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)


screen = s()
screen.exitonclick()
