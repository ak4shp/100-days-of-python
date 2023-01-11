import time
from turtle import Screen

from snake import Snake
from food import Food
from scoreboard import Scoreboard

#* Global Objects
screen = None
snake = None
food = None
scoreboard = None

#* game setup
def game_setup():
    global screen, snake, food, scoreboard
    
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("SNAKEython! ")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    user_name = screen.textinput("Welcome to SNAKEython!", "Who is going to play?")
    scoreboard.name = user_name

    screen.listen()
    screen.onkeypress(snake.up, "Up")
    screen.onkeypress(snake.down, "Down")
    screen.onkeypress(snake.left, "Left")
    screen.onkeypress(snake.right, "Right")

#* Game Play
def main():
    game_setup()
    game_on = True

    while game_on:
        screen.update()    #* Update screen after the hidden animation by (screen.tracer(0))
        time.sleep(0.12)     #* Update the screen in each 0.12 sec
        snake.move()

        #* Detect collision with food
        if snake.head.distance(food) < 14:
            food.refresh()
            scoreboard.increase_score()
            snake.increase_tail()

        #* Detect collision with wall
        if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
            game_on = False
            scoreboard.game_over() 

        #* Detect collision with tail
        for segment in snake.body_parts[3::]:
            if snake.head.distance(segment) < 19:
                game_on = False
                scoreboard.game_over()

#* Driver 
if __name__ == "__main__":
    main()
    screen.exitonclick()