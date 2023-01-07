from turtle import Turtle, Screen, colormode
import random
t = Turtle()
colormode(255)


"""Make colored random walk"""
def new_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

direction = [0, 90, 180, 270]
t.pensize(5)
t.speed("fastest")
# t.screen.screensize(20, 30)
for _ in range(500):
    col = new_color()
    t.color(col)
    t.setheading(random.choice(direction))
    t.forward(20)


"""Draw different shapes (nested)"""
# colors = ["Black", "CornflowerBlue", "Goldenrod", "Blue", "Red", "SpringGreen", "DodgerBlue", "Magenta"]
# for i in range(8):
#     shape_id = i + 3
#     angle = 360 // (shape_id)
#     t.pensize(2)
#     t.color(colors[i])
#     for _ in range(shape_id):
#         t.forward(70)
#         t.right(angle=angle)


"""Square with dashed line and dot"""
# for _ in range(4):
#     t.right(90)
#     for _ in range(20):
#         t.pendown()
#         t.forward(5)
#         t.penup()
#         t.dot()
#         t.forward(5)
#     t.dot()


"""Draw a star filled with colors"""
# t.shape("circle")
# t.color('red', 'yellow')
# t.begin_fill()

# while True:
#     t.forward(200)
#     t.left(100)
#     if abs(t.pos())<1:
#         break

# t.end_fill()

canvas = Screen()
canvas.exitonclick()
