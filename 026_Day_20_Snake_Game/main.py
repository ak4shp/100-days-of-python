from turtle import Turtle, Screen

#TODO 2: Move the snake
#TODO 3: Control the snake by arraw keys
#TODO 4: Detect collision with food
#TODO 5: Create a scoreboard
#TODO 6: Detect collision with wall
#TODO 7: Detect Collision with tail

#* Setup Screen 
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Real Python! Hishhhh...")

#TODO 1: Create a snake body
x_pos = 0
for i in range(3):
    t= Turtle(shape="square")
    t.penup()
    t.color("white")
    t.goto(x=x_pos, y=0)
    x_pos -= 20

screen.exitonclick()