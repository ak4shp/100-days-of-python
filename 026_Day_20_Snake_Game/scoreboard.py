from turtle import Turtle


ALIGNMENT = "center"
FONT = ('Courier', 20, 'bold')


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.name = ""
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Right Updated score to the scoreboard."""
        self.write(f"Hello {self.name} | Score = {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increases score by 1. Clears previous acore and writes updated score."""
        self.score += 1
        self.clear()
        self.update_scoreboard()
        
    def game_over(self):
        """Write 'Game Over' to the center of the game screen."""
        self.goto(0, 0)
        self.write(f"Game Over!!\nPress 'r' to resart.\nPress 'q' to quit.", move=False, align=ALIGNMENT, font=FONT)

    def quit_me(self, food:object, snake:object):
        self.clear()
        food.clear_screen()
        snake.clear_screen()
        self.goto(0, 0)
        self.write(f"Thank You💕 for using SNAKEython.", move=False, align=ALIGNMENT, font=FONT)
