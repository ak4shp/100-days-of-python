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
    screen.onkeypress(restart, "r")  
    screen.onkeypress(quit, "q")


#* Game Play
def main():
    global restart_game
    game_on = True
    game_setup()

    print("Game started.....")
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
            restart_game = True
            scoreboard.game_over() 

        #* Detect collision with tail
        for segment in snake.body_parts[3::]:
            if snake.head.distance(segment) < 19:
                game_on = False
                restart_game = True
                scoreboard.game_over()

#* Restart Game
restart_game = False
def restart():
    global restart_game
    if restart_game:
        screen.clear()
        restart_game = False
        print("Restarting....")
        main()

#* Quit Game
def quit():
    global restart_game
    if restart_game:
        print("Quitting")
        restart_game = False
        scoreboard.quit_me(food= food, snake= snake)
        screen.update()
        time.sleep(2)
        screen.bye()
        
#* Driver 
if __name__ == "__main__":
    main()
    screen.exitonclick()