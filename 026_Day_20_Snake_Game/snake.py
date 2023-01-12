from turtle import Turtle

MOVE_STEP = 20
SNAKE_POSITIONS = [(0, 0), (-20, 0), (-40, 0), (-60, 0)]
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
        self.tail = self.body_parts[-2]
        self.tail2 = self.body_parts[-1]
        self.tail.shape("circle")
        self.tail2.shape("circle")
        self.tail2.shapesize(0.7, 0.7)

    def create_snake(self):
        """Create A snake by merging all the Body Parts"""    
        for pos in SNAKE_POSITIONS:
            t = Turtle(shape="square")
            t.penup()
            t.color("white")
            t.goto(pos)
            self.body_parts.append(t)
        
    def increase_tail(self):
        """Add a new segment to the last position of snake's body."""
        last_x = self.body_parts[-1].xcor()
        last_y = self.body_parts[-1].ycor()
        pos = (last_x, last_y)
        new_t = Turtle(shape="square")
        new_t.penup()
        new_t.color("white")
        new_t.goto(pos)
        self.body_parts.insert(-2, new_t)

    def move(self):
        """Moves snake continuously""" 
        #! moving each nth segment to the position of (n-1)th segment
        for seg in range(len(self.body_parts)-1, 0, -1):
            new_x = self.body_parts[seg -1].xcor()
            new_y = self.body_parts[seg -1].ycor()
            self.body_parts[seg].goto(new_x, new_y)
        self.head.forward(MOVE_STEP)

    def up(self):
        """Turn UP | 'Up' arrow key"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Turn DOWN | 'Down' arrow key"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Turn LEFT | 'Left' arrow key"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Turn RIGHT | 'Right' arrow key"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def clear_screen(self):
        for t in self.body_parts:
            t.hideturtle()
        