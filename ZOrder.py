import turtle

def z_order_fractal(turtle, size, level):
    if level == 0:
        turtle.fd(size)
        return
    turtle.pensize(level)
    for angle in [0, 90, -90, 0]:
        turtle.left(angle)
        z_order_fractal(turtle, size/2, level-1)

# set up turtle
t = turtle.Turtle()
t.speed(0)

# move turtle to starting position
t.penup()
t.goto(-100, 100)
t.pendown()

# draw fractal
z_order_fractal(t, 200, 6)

# hide turtle
t.hideturtle()

# keep window open until closed manually
turtle.done()
