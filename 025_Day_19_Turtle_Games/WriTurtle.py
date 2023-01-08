from turtle import Turtle, Screen
import random

# Key Press Functions
class Movements:
    def __init__(self, turtle, screen) -> None:
        self.t = turtle
        self.screen = screen
        self.pen_size = 1
        self.pen_color = "Black"

    def fwd(self):        
        """10 step forward | key= 'Up' arrow."""
        self.t.forward(10)

    def bkwd(self): 
        """10 step backward | key= 'Down' arrow."""
        self.t.backward(10)

    def lft(self):
        """Turn left by 10 degree | key= 'Left' arrow."""
        self.t.left(10)

    def rght(self):
        """Turn right by 10 degree | key= 'Right' arrow."""
        self.t.right(10)

    def pen_size_incr(self):
        """Increase pen stroke by 1. Max upto 10 | key= 'a'"""
        # global pen_size
        if not self.pen_size >= 15:
            self.pen_size += 1
            self.t.pensize(self.pen_size)

    def pen_size_decr(self):
        """Decrease pen stroke by 1. Min upto 1 | key= 's'"""
        # global pen_size
        if not self.pen_size <= 1 :
            self.pen_size -= 1
            self.t.pensize(self.pen_size)

    def change_color(self):
        """Change pen stroke color randomly | Key= 'c'."""
        colors = ["Black", "CornflowerBlue", "Goldenrod", "Blue", "Red", "SpringGreen", "DodgerBlue", "Magenta"]
        self.pen_color = random.choice(colors)
        self.t.pencolor(self.pen_color)
        self.t.shape("classic")
        self.t.shapesize(outline = 1.2)

    def erasor(self):
        """Erasor (Change pen stroke color to White) | Key= 'e'."""
        self.t.pencolor("White")
        self.t.shape("arrow")


    def pen_up(self):
        """Free hand mode for movement of cursor | Key= 'f'."""
        self.t.penup()

    def pen_down(self):
        """Writing mode | Key= 'd'."""
        self.t.pendown()

    def reset_screen(self):
        """Clears all drawings and reintialises turtle | key= 'r'."""
        self.screen.reset()
        


def start():
    """Initialises objects"""
    t = Turtle()
    screen = Screen()
    movement = Movements(turtle=t, screen=screen)
    return t, screen, movement


# Key press Events
def main():
    # t.write("WriTurtle", font= ('Arial',12,'bold'))
    t, screen, opration = start()
    t.color(opration.pen_color)
    t.pensize(opration.pen_size)
    screen.onkeypress(opration.fwd, "Up")
    screen.onkeypress(opration.bkwd, "Down")
    screen.onkeypress(opration.lft, "Left")
    screen.onkeypress(opration.rght, "Right")
    screen.onkeypress(opration.pen_size_incr, "a")
    screen.onkeypress(opration.pen_size_decr, "s")
    screen.onkeypress(opration.change_color, "c")
    screen.onkeypress(opration.erasor, "e")
    screen.onkeypress(opration.pen_up, "f")
    screen.onkeypress(opration.pen_down, "d")
    screen.onkeypress(opration.reset_screen, "r")

    screen.listen()
    screen.exitonclick()    
    
main()


"""
************ Navigation ************

(OPERATION --> KEY)
Forward --> "Up" 
Backward --> "Down" 
Turn Left --> "Left" 
Turn Right--> "Right" 
Increase Pen stroke --> "a" 
Decrease Pen stroke --> "s" 
Change Pen stroke color --> "c" 
Erasor --> "e" 
Turn Off stroke --> "f" 
Turn On stroke --> "d" 
Clear all drawing --> "r" 
...
"""