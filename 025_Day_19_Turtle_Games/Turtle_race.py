from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
bet_turtle = screen.textinput(title="Turtle Race", prompt="Which Turtle is yours? (Red, Blue, Black, Orange, Green, Purple) ")

colors = ["Red", "Blue", "Black", "Orange", "Green", "Purple"]
all_turtles = []
y_pos = -120
winner = ""

for i in range(6):
    t = Turtle(shape="turtle")
    t.penup()
    t.goto(x=-230, y=y_pos)
    t.color(colors[i])
    y_pos += 40
    all_turtles.append(t)

if bet_turtle:
    is_race_on = True

while is_race_on:
    for tim in all_turtles:
        if tim.xcor() > 230:
            winner = tim.pencolor()
            is_race_on = False
        dist = random.randint(0, 10)
        tim.forward(dist)

if bet_turtle.lower() == winner.lower():
    print(f"You Won !", end= " ") 
else:
    print("You Lose !", end= " ")
print(f"{winner} finished the race first.")

screen.exitonclick()