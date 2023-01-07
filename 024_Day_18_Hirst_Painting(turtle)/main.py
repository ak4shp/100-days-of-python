from turtle import Turtle, Screen, colormode
import random

t = Turtle()
colormode(255)
color_list = [(207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 49), (221, 207, 105),
              (132, 177, 203), (158, 46, 83), (45, 55, 104), (169, 160, 39), (129, 189, 143),
              (83, 20, 44), (37, 43, 67), (186, 94, 107), (187, 140, 170), (85, 120, 180),
              (59, 39, 31), (88, 157, 92), (78, 153, 165), (194, 79, 73), (45, 74, 78),
              (80, 74, 44), (161, 201, 218), (57, 125, 121), (219, 175, 187), (169, 206, 172), (219, 182, 169)]


t.speed("fastest")
t.penup()
t.hideturtle()
t.setheading(225)
t.forward(350)
t.setheading(0)

total_dots = 100
for dot_ct in range(1, total_dots + 1):
    dot_color = random.choice(color_list)
    t.dot(20, dot_color)
    t.forward(50)

    if dot_ct % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)

canvas = Screen()
canvas.exitonclick()