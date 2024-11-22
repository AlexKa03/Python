from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("black") # Personal touch

colors = ["red", "green", "blue", "orange", "purple", "yellow"]
y_position = [-70, -40, -10, 20, 50, 80]

user_selection = screen.textinput(title="Make your bet",
                                  prompt="Which turtle will win the race? Red, Green, Blue, Orange, Purple or Yellow: ").lower()

# # Prompt user to select a valid color / personal touch
while user_selection not in colors:
    user_selection = screen.textinput(title="Invalid Color",
                                      prompt="Invalid color! Please choose one of these colors: Red, Green, Blue, Orange, Purple or Yellow: ").lower()

turtles = []
for i in range(0, 6):
    turtles.append(Turtle(shape="turtle"))
    turtles[i].penup()
    turtles[i].color(colors[i])
    turtles[i].goto(x=-230, y=y_position[i])

# Create a turtle for displaying text / personal touch
result_turtle = Turtle()
result_turtle.hideturtle()
result_turtle.penup()

if user_selection:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            result_turtle.goto(0, 150)
            if winning_color == user_selection:
                result_turtle.color(winning_color)
                result_turtle.write(f"You've WON! The {winning_color} turtle is the winner!", align="center",
                                    font=("Arial", 16, "bold"))
            else:
                result_turtle.color(winning_color)
                result_turtle.write(f"You've LOST! The {winning_color} turtle is the winner!", align="center",
                                    font=("Arial", 16, "bold"))
            break # Exit loop to stop race/ personal touch

        random_distance = random.randint(0, 10)
        turtle. forward(random_distance)

screen.exitonclick()