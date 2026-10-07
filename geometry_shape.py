# Vajaran Nall

import turtle

SQUARE = "1"
CIRCLE = "2"
TRIANGLE = "3"
QUIT = "4"

def main():
    #TODO: reference lecture5 slide#65 to call the function to draw the requested shape until user chooses to quit

    choice = "0"

    while choice != QUIT:
        display_menu()
        choice = input("Choose a shape to draw: ")

        if choice == SQUARE:
            print("Where should I start drawing the square?")
            x = float(input("Enter the starting X coordinate? "))
            y = float(input("Enter the starting Y coordinate? "))
            side = float(input("How long should each of the square's three sides be? "))
            color = input("What color should the square be? ")
            square(x, y, side, color)

        elif choice == CIRCLE:
            print("Where should I start drawing the circle?")
            x = float(input("Enter the starting X coordinate: "))
            y = float(input("Enter the starting Y coordinate: "))            
            radius = float(input("Enter the circle's radius: "))
            color = input("What color should your circle be? ")
            circle(x, y, radius, color)

        elif choice == TRIANGLE:
            print("Where should I start drawing the triangle?")
            x = float(input("Enter the starting X coordinate: "))
            y = float(input("Enter the starting Y coordinate: "))
            side = float(input("How long should each of the triangle's three sides be? "))
            color = input("What color should the triangle be? ")
            equilateral_triangle(x, y, side, color)

        elif choice == QUIT:
            print("Exiting the program...")

        else:
            print("Error: Invalid Selection.")
    turtle.done()



def display_menu():
    print()
    print("Shape Menu")
    print("1) Draw a Square")
    print("2) Draw a Circle")
    print("3) Draw an Equilateral Triangle")
    print("4) Quit")

#TODO: copy the code from lecture5 slide# 69
def square(x, y, side, color):
    turtle.penup()
    turtle.goto(x, y)       # Move to (X, Y)
    turtle.fillcolor(color) # Set the fill color
    turtle.pendown()        # Lower the pen
    turtle.begin_fill()     # Begin fill
    for count in range(4):
        turtle.forward(side)
        turtle.left(90)
    turtle.end_fill()


def equilateral_triangle(x, y, side, color):
    # draw a triangle starting coordinate at x,y
    turtle.penup()              
    turtle.goto(x, y)           
    turtle.fillcolor(color)     
    turtle.pendown()            
    turtle.begin_fill()         
    for count in range(3):      
        turtle.forward(side)
        turtle.left(120)
    turtle.end_fill()

#TODO: copy lecture slide 71 code
def circle(x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

if __name__ == "__main__":
    main()