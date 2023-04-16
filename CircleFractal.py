import turtle
import math

def circle_fractal(turtle, depth, radius):
    if depth == 0:
        turtle.circle(radius)
    else:
        for angle in [0, 60, 120, 180, 240, 300]:
            x = radius * math.cos(math.radians(angle))
            y = radius * math.sin(math.radians(angle))
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()
            circle_fractal(turtle, depth - 1, radius / 3)

if __name__ == '__main__':
    # Initialize the turtle
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(0, -200)
    t.pendown()

    # Draw the circle fractal
    circle_fractal(t, 3, 150)

    # Keep the window open until it is closed
    turtle.mainloop()
