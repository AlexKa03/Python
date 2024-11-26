from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(x= 0, y= 270)
        self.color("white")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score = {self.score}", move=False, align=ALIGNMENT, font=FONT)
        self.score += 1