from turtle import Turtle


class Label(Turtle):
    def __init__(self, state, x_coor, y_coor):
        super(Label, self).__init__()
        self.hideturtle()
        self.penup()
        self.goto(x_coor, y_coor)
        self.write(f"{state}", align="center")





