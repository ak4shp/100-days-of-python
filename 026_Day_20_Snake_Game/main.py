import time
from turtle import Screen
from snake import Snake
from food import Food

#TODO 1: Create a snake -> done
#TODO 2: Move the snake -> done
#TODO 3: Control the snake by arraw keys -> done
#TODO 4: Detect collision with food -> done
#TODO 5: Create a scoreboard
#TODO 6: Detect collision with wall
#TODO 7: Detect Collision with tail

#* Setup Screen 
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Real Python! Hishhhh...")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

game_on = True
while game_on:
    screen.update()    #* Shows the Hiden animation by (screen.tracer(0))
    time.sleep(0.15)     #* Update the screen in each 0.2 sec
    snake.move()

    if snake.head.distance(food) < 14:
        food.refresh()

screen.exitonclick()