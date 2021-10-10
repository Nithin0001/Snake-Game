from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time


screen = Screen()
screen.setup(width=1280, height=720)
screen.bgcolor("#dfcfbe")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.11)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    if snake.head.xcor() > 620 or snake.head.xcor() < -620 or snake.head.ycor() > 340 or snake.head.ycor() < -340:
        score.game_over()
        game_is_on = False
    for bl in snake.block[1:]:
        if snake.head.distance(bl) < 10:
            score.game_over()
            game_is_on = False

screen.exitonclick()
