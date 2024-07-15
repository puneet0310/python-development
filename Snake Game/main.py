from turtle import Screen,Turtle
from snake import Snake
import time
from food import Food
from scoreboard import Score
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake= Snake()
food=Food()
screen.listen()
score=Score()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")




game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()



    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score.inc_score()
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280 :
        game_is_on=False
        score.game_over()

    for segments in snake.segments:
        if segments == snake.head:
            pass
        if segments != snake.head:
            if snake.head.distance(segments)<10:
                game_is_on=False
                score.game_over()

        































screen.exitonclick()