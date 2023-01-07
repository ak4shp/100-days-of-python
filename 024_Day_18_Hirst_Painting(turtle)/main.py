from turtle import Turtle, Screen
import random
t = Turtle()

"""Square with dashed line and dot"""
for _ in range(4):
    t.right(90)
    for _ in range(20):
        t.pendown()
        t.forward(5)
        t.penup()
        t.dot()
        t.forward(5)
    t.dot()


"""Make colored random drawing"""
# colors = ["OrangeRed", "MediumSpringGreen", "DodgerBlue", "LightGreen", "HotPink"]
# direction = [0, 90, 180, 270]
# direction2 = [90, 180, 270]

# t.pensize(2)
# # t.speed("fastest")
# t.screen.screensize(200, 300)
# # for _ in range(500):
# #     t.color(random.choice(colors))
# #     if t.ycor() >= 300 or t.xcor() >= 200:
# #         t.setheading(random.choice(direction2))
# #     else:
# #         t.setheading(random.choice(direction))
# #     t.forward(20)


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
