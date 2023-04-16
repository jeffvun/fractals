import turtle
import math


def draw_circle(x, y, r):
    turtle.penup()
    turtle.goto(x, y - r)
    turtle.pendown()
    turtle.circle(r)


def apollonian_gasket(c1, c2, c3, depth):
    if depth == 0:
        return
    draw_circle(c1[0], c1[1], c1[2])
    draw_circle(c2[0], c2[1], c2[2])
    draw_circle(c3[0], c3[1], c3[2])
    c12 = (c1[0] + c2[0], c1[1] + c2[1], c1[2] + c2[2])
    c13 = (c1[0] + c3[0], c1[1] + c3[1], c1[2] + c3[2])
    c23 = (c2[0] + c3[0], c2[1] + c3[1], c2[2] + c3[2])
    apollonian_gasket(c1, c12, c13, depth - 1)
    apollonian_gasket(c2, c12, c23, depth - 1)
    apollonian_gasket(c3, c13, c23, depth - 1)


turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("white")
c1 = (-200, 0, 150)
c2 = (200, 0, 150)
c3 = (0, 200, 150)
apollonian_gasket(c1, c2, c3, 5)
turtle.done()
