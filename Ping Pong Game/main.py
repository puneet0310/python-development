from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
import time

screen=Screen()
screen.bgcolor("Black")
screen.setup(width=800,height=600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle= Paddle((0,0))
l_paddle= Paddle((0,0))
r_paddle.goto(350,0)
l_paddle.goto(-350,0)
ball=Ball()



   

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"8")
screen.onkey(l_paddle.go_down,"2")
game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()


    if ball.ycor()>270 or ball.ycor()<-270:
        ball.bounce_y()


    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()
    
    if ball.xcor()>380:
        ball.reset_position()
    if ball.xcor()<-380:
        ball.reset_position()
        




screen.exitonclick()