import turtle


def draw_plant(axiom, rules, angle, length, iterations):
    state = axiom
    for i in range(iterations):
        new_state = ""
        for char in state:
            if char in rules:
                new_state += rules[char]
            else:
                new_state += char
        state = new_state

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.left(90)

    stack = []
    for char in state:
        if char == 'F':
            t.forward(length)
        elif char == '+':
            t.right(angle)
        elif char == '-':
            t.left(angle)
        elif char == '[':
            stack.append((t.heading(), t.position()))
            t.left(angle)
        elif char == ']':
            heading, position = stack.pop()
            t.penup()
            t.goto(position)
            t.setheading(heading)
            t.pendown()

    turtle.done()


axiom = "X"
rules = {
    "X": "F+[[X]-X]-F[-FX]+X",
    "F": "FF"
}
angle = 25
length = 5
iterations = 5

draw_plant(axiom, rules, angle, length, iterations)
