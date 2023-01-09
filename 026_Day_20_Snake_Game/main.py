from turtle import Turtle, Screen
import time
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
screen.tracer(0)

#TODO 1: Create a snake body
body_parts = []
x_pos = 0
for i in range(3):
    t = Turtle(shape="square")
    t.penup()
    t.color("white")
    t.goto(x=x_pos, y=0)
    x_pos -= 20
    body_parts.append(t)


#TODO 2: Move the snake
game_on = True
while game_on:
    screen.update()    #* Shows the Hiden animation by (screen.tracer(0))
    time.sleep(0.2)

    #! moving each nth segment to the position of (n-1)th segment
    for seg in range(len(body_parts)-1, 0, -1):
        new_x = body_parts[seg -1].xcor()
        new_y = body_parts[seg -1].ycor()
        body_parts[seg].goto(new_x, new_y)
    body_parts[0].forward(20)


screen.exitonclick()