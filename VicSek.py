import turtle

def vicsek_fractal(t, depth, size):
    if depth == 0:
        t.begin_fill()
        for _ in range(4):
            t.forward(size)
            t.left(90)
        t.end_fill()
        return
    vicsek_fractal(t, depth-1, size/3)
    t.forward(size/3)
    vicsek_fractal(t, depth-1, size/3)
    t.forward(size/3)
    vicsek_fractal(t, depth-1, size/3)
    t.backward(size/3*2)
    vicsek_fractal(t, depth-1, size/3)
    t.forward(size/3)
    vicsek_fractal(t, depth-1, size/3)
    t.backward(size/3)
    vicsek_fractal(t, depth-1, size/3)
    t.backward(size/3)
    vicsek_fractal(t, depth-1, size/3)
    t.forward(size/3)
    vicsek_fractal(t, depth-1, size/3)
    t.backward(size/3)
    vicsek_fractal(t, depth-1, size/3)
    t.forward(size/3)
    t.forward(size/3)

if __name__ == '__main__':
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-150, 150)
    t.pendown()
    t.color('black', 'white')
    t.begin_fill()
    for _ in range(4):
        t.forward(300)
        t.left(90)
    t.end_fill()
    t.color('black')
    vicsek_fractal(t, 4, 300)
    turtle.done()
