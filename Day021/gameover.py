from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(x=0, y=0)
        self.color("white")
        self.hideturtle()

    def end_screen(self):
        self.write(arg=f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)