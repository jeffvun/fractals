import turtle


def sierpinski_triangle(t, length, depth):
    if depth == 0:
        for i in range(3):
            t.forward(length)
            t.left(120)
    else:
        sierpinski_triangle(t, length / 2, depth - 1)
        t.forward(length / 2)
        sierpinski_triangle(t, length / 2, depth - 1)
        t.backward(length / 2)
        t.left(60)
        t.forward(length / 2)
        t.right(60)
        sierpinski_triangle(t, length / 2, depth - 1)
        t.left(60)
        t.backward(length / 2)
        t.right(60)


# Set up the turtle graphics
t = turtle.Turtle()
t.speed('fastest')
t.penup()
t.goto(-200, -200)
t.pendown()

# Generate the Sierpinski triangle
length = 400
depth = 4
for i in range(3):
    sierpinski_triangle(t, length, depth)
    length -= 100
    depth -= 1

# Clean up the turtle graphics
t.hideturtle()
turtle.done()
