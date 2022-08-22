from turtle import Turtle

STRETCH_WIDTH = 5
STRETCH_HEIGHT = 1
MOVE_LIMIT = 20


class Paddle(Turtle):

    def __init__(self, position):
        super(Paddle, self).__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=STRETCH_WIDTH, stretch_len=STRETCH_HEIGHT)
        self.penup()
        self.goto(position)

    def up(self):
        new_y = self.ycor() + MOVE_LIMIT
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - MOVE_LIMIT
        self.goto(self.xcor(), new_y)

