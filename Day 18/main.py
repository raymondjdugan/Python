from turtle import Screen as s, Turtle as t
from random import randint
timmy_the_turtle = t()

# timmy_the_turtle.pen(fillcolor="black", pencolor="red", pensize=5)

# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(90)

# for i in range(15):
#     timmy_the_turtle.forward(10)
#     if i % 2 == 0:
#         timmy_the_turtle.up()
#     else:
#         timmy_the_turtle.down()

screen = s()
screen.colormode(255)


def create_shape(side):
    timmy_the_turtle.pencolor(
        randint(0, 255), randint(0, 255), randint(0, 255))
    for _ in range(side):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(360/side)


for shape_side_n in range(3, 10):
    create_shape(shape_side_n)


screen.exitonclick()
