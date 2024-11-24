from turtle import Turtle

BODY_PART_POSITION = -20
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for i in range(0, 3):
            self.snake_body.append(Turtle(shape="square"))
            self.snake_body[i].penup()
            self.snake_body[i].color("white")
            self.snake_body[i].goto(y=0, x=i * (BODY_PART_POSITION))

    def move(self):
        for body in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[body - 1].xcor()
            new_y = self.snake_body[body - 1].ycor()
            self.snake_body[body].goto(new_x, new_y)
        self.snake_body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)