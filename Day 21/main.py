from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

Y_COR_COLLISION = 280
X_COR_COLLISION = 320
SCREEN_LIMIT = 380
X_PADDLE_DISTANCE = 50

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Raymond's Python Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > Y_COR_COLLISION or ball.ycor() < -Y_COR_COLLISION:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(r_paddle) < X_PADDLE_DISTANCE and ball.xcor() > X_COR_COLLISION \
            or ball.distance(l_paddle) < X_PADDLE_DISTANCE and ball.xcor() < -X_COR_COLLISION:
        ball.bounce_x()

    if ball.xcor() > SCREEN_LIMIT:
        ball.reset_position()

    if ball.xcor() < -SCREEN_LIMIT:
        ball.reset_position()

screen.exitonclick()
