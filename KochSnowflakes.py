import turtle

def koch_snowflake(length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        length /= 3.0
        koch_snowflake(length, depth-1)
        turtle.left(60)
        koch_snowflake(length, depth-1)
        turtle.right(120)
        koch_snowflake(length, depth-1)
        turtle.left(60)
        koch_snowflake(length, depth-1)

def main():
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-150, 90)
    turtle.pendown()
    turtle.color("blue")
    for i in range(3):
        koch_snowflake(300, 4)
        turtle.right(120)
    turtle.done()

if __name__ == '__main__':
    main()
