from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 20, 'bold')


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score = {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", move=False, align=ALIGNMENT, font=FONT)

