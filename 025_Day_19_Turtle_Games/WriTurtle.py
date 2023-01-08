from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()

# Key Press Functions
class Movements:
    def __init__(self) -> None:
        self.pen_size = 1
        self.pen_color = "Black"

    def fwd(self):        
        """10 step forward | key= 'Up' arrow."""
        t.forward(10)

    def bkwd(self): 
        """10 step backward | key= 'Down' arrow."""
        t.backward(10)

    def lft(self):
        """Turn left by 10 degree | key= 'Left' arrow."""
        t.left(10)

    def rght(self):
        """Turn right by 10 degree | key= 'Right' arrow."""

        t.right(10)

    def pen_size_incr(self):
        """Increase pen stroke by 1. Max upto 10 | key= 'a'"""
        # global pen_size
        if not self.pen_size >= 10:
            self.pen_size += 1
            t.pensize(self.pen_size)

    def pen_size_decr(self):
        """Decrease pen stroke by 1. Min upto 1 | key= 's'"""
        # global pen_size
        if not self.pen_size <= 1 :
            self.pen_size -= 1
            t.pensize(self.pen_size)

    def change_color(self):
        """Change pen stroke color randomly | Key= 'c'."""
        colors = ["Black", "CornflowerBlue", "Goldenrod", "Blue", "Red", "SpringGreen", "DodgerBlue", "Magenta"]
        self.pen_color = random.choice(colors)
        t.color(self.pen_color)

    def erasor(self):
        """Erasor (Change pen stroke color to White) | Key= 'e'."""
        t.color("White")

    def pen_up(self):
        """Free hand mode for movement of cursor | Key= 'f'."""
        t.penup()

    def pen_down(self):
        """Writing mode | Key= 'd'."""
        t.pendown()

    def clear_screen(self):
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