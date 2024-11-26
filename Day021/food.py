from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("purple")
        self.speed("fastest")
        self.spawn_new_food()


    def spawn_new_food(self):
        # Personal touch 
        # Align to the grid by rounding to the nearest 20
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)

        # Snap to the 20x20 grid
        snapped_x = round(random_x / 20) * 20
        snapped_y = round(random_y / 20) * 20

        self.goto(snapped_x, snapped_y)