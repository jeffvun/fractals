import turtle

def fractal_tetrahedron(turtle, depth, length):
    if depth == 0:
        for _ in range(3):
            turtle.forward(length)
            turtle.left(120)
    else:
        for angle in [0, 120, -120]:
            fractal_tetrahedron(turtle, depth - 1, length / 2)
            turtle.forward(length / 2)
            turtle.left(angle)
            turtle.forward(length / 2)
            turtle.right(angle)

if __name__ == '__main__':
    # Initialize the turtle
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-150, -150)
    t.pendown()

    # Draw the fractal tetrahedron
    fractal_tetrahedron(t, 3, 300)

    # Keep the window open until it is closed
    turtle.mainloop()
