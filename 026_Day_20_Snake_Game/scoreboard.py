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
        self.increase_score()

    def increase_score(self):
        self.write(f"Score = {self.score}", move=False, align=ALIGNMENT, font=FONT)