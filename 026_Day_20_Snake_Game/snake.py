from turtle import Turtle

MOVE_STEP = 20
SNAKE_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self) -> None:
        self.body_parts = []
        self.create_snake()
        self.head = self.body_parts[0]
        self.head.color("red")
        self.head.shape("turtle")

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
        self.head.forward(MOVE_STEP)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        