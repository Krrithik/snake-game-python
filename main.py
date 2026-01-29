from food import Food
from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_on = True
while game_on:
    snake.move()
    screen.update()
    time.sleep(0.1)

#     Detect collision of snake and food
    if snake.head.distance(food) < 25:
        print("nom nom nom")
        snake.increase_height()
        food.change_pos()

screen.update()
screen.exitonclick()