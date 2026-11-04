# Vajaran Nall

import turtle

def render_diamond(pen, center_x, center_y, radius, color):
    pen.penup()
    pen.goto(center_x, center_y + radius)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()

    for x, y in [
        (center_x + radius, center_y),
        (center_x, center_y - radius),
        (center_x - radius, center_y),
        (center_x, center_y + radius),
    ]:
        pen.goto(x, y)

    pen.end_fill()

def main():
    screen = turtle.Screen()
    screen.title("Double Diamonds")
    screen.setup(width=520, height=350)
    screen.bgcolor("white")

    pen = turtle.Turtle()
    pen.speed(3)
    pen.pensize(2)
    pen.pencolor("black")

    radius = 105
    render_diamond(pen, -radius, 0, radius, "blue")
    render_diamond(pen, radius, 0, radius, "blue")

    pen.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()
