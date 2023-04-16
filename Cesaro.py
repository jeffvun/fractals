import turtle

def cesaro_fractal(turtle, depth, length):
    if depth == 0:
        turtle.forward(length)
    else:
        for angle in [85, -170, 85, 0]:
            cesaro_fractal(turtle, depth - 1, length / 3)
            turtle.left(angle)

if __name__ == '__main__':
    # Initialize the turtle
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-200, 0)
    t.pendown()

    # Draw the Cesaro fractal
    cesaro_fractal(t, 4, 400)

    # Keep the window open until it is closed
    turtle.mainloop()
