from turtle import Turtle

MOVE_STEP = 20
SNAKE_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self) -> None:
        self.body_parts = []
        self.create_snake()

    def create_snake(self):    
        for pos in SNAKE_POSITIONS:
            t = Turtle(shape="square")
            t.penup()
            t.color("white")
            t.goto(pos)
            self.body_parts.append(t)

    def move(self): 
        #! moving each nth segment to the position of (n-1)th segment
        for seg in range(len(self.body_parts)-1, 0, -1):
            new_x = self.body_parts[seg -1].xcor()
            new_y = self.body_parts[seg -1].ycor()
            self.body_parts[seg].goto(new_x, new_y)
        self.body_parts[0].forward(MOVE_STEP)
