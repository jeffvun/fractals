import turtle

def koch_curve(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, length/3, depth-1)
            t.left(angle)

# Set up the turtle graphics
t = turtle.Turtle()
t.speed('fastest')
t.penup()
t.goto(-200, 0)
t.pendown()

# Generate the Koch curve
length = 400
depth = 4
koch_curve(t, length, depth)

# Clean up the turtle graphics
t.hideturtle()
turtle.done()
