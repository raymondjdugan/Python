import random
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.back(10)


def turn_right():
    tim.right(10)


def turn_left():
    tim.left(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


tim.hideturtle()
tim.pendown()
screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")

# tim = Turtle()
# screen = Screen()
# screen.colormode(255)
# screen.setup(width=500, height=400)
# user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color: ")
# y_positions = [-70, -40, -10, 20, 50, 80]
# all_turtles = []
#
# for turtle_index in range(0, 6):
#     colors = ['blue', 'green', 'red', 'yellow', 'pink', 'violet']
#     new_turtle = Turtle(shape="turtle")
#     new_turtle.color(colors[turtle_index])
#     new_turtle.penup()
#     new_turtle.goto(x=-230, y=y_positions[turtle_index])
#     all_turtles.append(new_turtle)
#
# if user_bet:
#     is_race_on = True
#
# while is_race_on:
#     for turtle in all_turtles:
#         if turtle.xcor() > 200:
#             is_race_on = False
#             winning_color = turtle.pencolor()
#             if winning_color == user_bet:
#                 print(f"You've won! The {winning_color} turtle is the winner!")
#             else:
#                 print(f"You've lost! The {winning_color} turtle is the winner!")
#
#         rand_distance = random.randint(1, 10)
#         turtle.forward(rand_distance)




screen.exitonclick()
