import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

#TODO 1: Create a snake -> done
#TODO 2: Move the snake -> done
#TODO 3: Control the snake by arraw keys -> done
#TODO 4: Detect collision with food -> done
#TODO 5: Create a scoreboard -> done
#TODO 6: Detect collision with wall -> done
#TODO 7: Detect Collision with tail

#* Setup Screen 
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Real Python! Hishhhh...")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    #* Detect collision with food
    if snake.head.distance(food) < 14:
        food.refresh()
        scoreboard.increase_score()
        snake.increase_tail()

    #* Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over() 

     #* Detect collision with tail
    for segment in snake.body_parts:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 19:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()