import turtle


def draw_kite(length):
    turtle.forward(length)
    turtle.right(72)
    turtle.forward(length)
    turtle.right(108)
    turtle.forward(length)
    turtle.right(72)
    turtle.forward(length)


def draw_dart(length):
    turtle.forward(length)
    turtle.right(144)
    turtle.forward(length)
    turtle.right(36)
    turtle.forward(length)
    turtle.right(144)
    turtle.forward(length)
    turtle.right(144)
    turtle.forward(length)
    turtle.right(36)
    turtle.forward(length)
    turtle.right(144)


def penrose_tiling(length, depth):
    if depth == 0:
        return

    # draw a kite
    draw_kite(length)

    # move to the next position
    turtle.right(72)
    turtle.forward(length)
    turtle.right(216)

    # draw a dart
    draw_dart(length)

    # move to the next position
    turtle.left(72)
    turtle.forward(length)
    turtle.right(144)
    turtle.forward(length)
    turtle.right(144)

    # recursively draw the next level
    penrose_tiling(length / 2, depth - 1)

    # move to the next position
    turtle.right(72)
    turtle.forward(length)
    turtle.right(144)
    turtle.forward(length)
    turtle.right(144)

    # draw another dart
    draw_dart(length)

    # move to the next position
    turtle.left(72)
    turtle.forward(length)
    turtle.right(216)

    # draw another kite
    draw_kite(length)

    # move to the next position
    turtle.right(72)
    turtle.forward(length)
    turtle.right(144)
    turtle.forward(length)
    turtle.right(144)

    # recursively draw the next level
    penrose_tiling(length / 2, depth - 1)

    # move to the next position
    turtle.right(72)
    turtle.forward(length)
    turtle.right(216)
    turtle.forward(length)
    turtle.right(144)
    turtle.forward(length)
    turtle.left(144)


# set up the turtle
turtle.speed(0)
turtle.hideturtle()
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()

# draw the Penrose tiling
penrose_tiling(200, 4)

# keep the turtle window open
turtle.done()
