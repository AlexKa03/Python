from turtle import Screen
from snake import Snake
from food import Food
from score import Score
from gameover import GameOver
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My Snake Game")

snake = Snake()
food = Food()
scoreboard = Score()
game_over = GameOver()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.update()
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect Collision with the food
    if snake.head.distance(food) < 15:
        food.spawn_new_food()
        snake.extend()
        scoreboard.update_score()

    # Detect Collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        game_over.end_screen()

    # Detect collision with the tail, note that due to mechanics the snakes head cant hit second and third element
    for body in snake.snake_body[3:]:
        if snake.head.distance(body) < 10:
            game_is_on = False
            game_over.end_screen()

screen.exitonclick()