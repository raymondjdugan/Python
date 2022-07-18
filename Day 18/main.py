from turtle import Screen as s, Turtle as t
import random
timmy_the_turtle = t()
screen = s()
screen.colormode(255)

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

# def create_shape(side):
#     timmy_the_turtle.pencolor(
#         randint(0, 255), randint(0, 255), randint(0, 255))
#     for _ in range(side):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(360/side)


# for shape_side_n in range(3, 10):
#     create_shape(shape_side_n)


# directions = [0, 90, 180, 270]
# timmy_the_turtle.pensize(15)
# timmy_the_turtle.speed("fastest")

# for _ in range(200):
#     timmy_the_turtle.color(random.randint(
#         0, 255), random.randint(0, 255), random.randint(0, 255))
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.setheading(random.choice(directions))


# timmy_the_turtle.speed("fastest")
# for x in range(1, 360, 6):
#     timmy_the_turtle.pencolor(random.randint(
#         1, 255), random.randint(1, 255), random.randint(1, 255))
#     timmy_the_turtle.seth(x)
#     timmy_the_turtle.circle(100)


screen.exitonclick()
