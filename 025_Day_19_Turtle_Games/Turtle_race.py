from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
my_turtle = screen.textinput(title="Turtle Race", prompt="Which Turtle is yours? ")

colors = ["Red", "Blue", "Black", "Orange", "Green", "Purple"]
y_pos = -120
all_turtles = []

for i in range(6):
    t = Turtle(shape="turtle")
    t.penup()
    t.goto(x=-230, y=y_pos)
    t.color(colors[i])
    y_pos += 40
    all_turtles.append(t)

# print(my_turtle)


screen.exitonclick()