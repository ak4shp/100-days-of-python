from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()

# Global Variables
pen_size = 1
pen_color = "Black"

t.color(pen_color)
t.pensize(pen_size)

# Key Press Functions
def fwd():        
    """10 step forward | 'Up' arrow."""
    t.forward(10)

def bkwd(): 
    """10 step backward | key= 'Down' arrow."""
    t.backward(10)

def lft():
    """Turn left by 10 degree | key= 'Left' arrow."""
    t.left(10)

def rght():
    """Turn right by 10 degree | key= 'Right' arrow."""

    t.right(10)

def pen_size_incr():
    """Increase pen stroke by 1. Max upto 10 | key= 'a'"""
    global pen_size
    if not pen_size >= 10:
        pen_size += 1
        t.pensize(pen_size)


def pen_size_decr():
    """Decrease pen stroke by 1. Min upto 1 | key= 's'"""
    global pen_size
    if not pen_size <= 1 :
        pen_size -= 1
        t.pensize(pen_size)

def change_color():
    """Change pen stroke color randomly | Key= 'c'."""
    global pen_color
    colors = ["Black", "CornflowerBlue", "Goldenrod", "Blue", "Red", "SpringGreen", "DodgerBlue", "Magenta"]
    pen_color = random.choice(colors)
    t.color(pen_color)

def erasor():
    """Erasor (Change pen stroke color to White) | Key= 'e'."""
    t.color("White")

def pen_up():
    """Free hand mode for movement of cursor | Key= 'f'."""
    t.penup()

def pen_down():
    """Writing mode | Key= 'd'."""
    t.pendown()

def clear_screen():
    """Clears all drawing | key= 'q'."""
    screen.clear()


# Key press Events
def main():
    # t.write("WriTurtle", font= ('Arial',12,'bold'))
    opr = Movements()
    t.color(opr.pen_color)
    t.pensize(opr.pen_size)
    screen.onkeypress(opr.fwd, "Up")
    screen.onkeypress(opr.bkwd, "Down")
    screen.onkeypress(opr.lft, "Left")
    screen.onkeypress(opr.rght, "Right")
    screen.onkeypress(opr.pen_size_incr, "a")
    screen.onkeypress(opr.pen_size_decr, "s")
    screen.onkeypress(opr.change_color, "c")
    screen.onkeypress(opr.erasor, "e")
    screen.onkeypress(opr.pen_up, "f")
    screen.onkeypress(opr.pen_down, "d")
    screen.onkeypress(opr.clear_screen, "q")

    screen.listen()

main()
screen.exitonclick()