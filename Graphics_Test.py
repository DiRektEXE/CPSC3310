# Turtle Graphics Test Experiment

import turtle

# Move forward by 100 pixels.
turtle.forward(100) 

# Turn Left / Right by (x) degrees
# Initial heading is 0 degrees
turtle.left(90)
turtle.right(90)

# Set Heading to a specific angle
turtle.setheading(270)

# Raise or Set the pen down
# When the turtle's pen is up it does not draw as it moves
turtle.penup()
turtle.pendown()

# Draw circle
radius = 100
turtle.circle(radius)

# Draw a dot at the turtle's current location
turtle.dot()

# Change turtle's pen color and size (line thickness)
turtle.pencolor('red')
# Default pensize is 1
turtle.pensize(5)

# Change window background color
# Color list is in textbook
turtle.bgcolor('green')

# Change turtle window size in pixels
# turtle.setup(width, height)
turtle.setup(640, 480)

# Erase everything in the graphics window
# Resets drawing color to black
# Resets turtle position to center of screen
# Does NOT reset the window background color  
turtle.reset()

# Only erases all drawings
turtle.clear()

# This is turtle.reset() except everything is reset (cleanest way)
turtle.clearscreen()

# Turtle uses cartesian coordinates.
# Move the turtle to a specific locaation with turtle.goto(x, y)
turtle.goto(0, 100)
# Get turtle's current position 
turtle.pos()
# Get current turtle X coordinate
turtle.xcor()
# Get current turtle Y coordinate
turtle.ycor()

# Change turtle animation speed | Range is 1 to 10 with 1 being the slowest
# If you specify 0 as the speed, all moves are instant (animation is disabled)
turtle.speed(10)

# Show / Hide turtle icon
turtle.showturtle()
turtle.hideturtle()

# Write text
# Lower left corner of the first character will be at the turtle's XY coordinates
turtle.write("Text")

# Fill shapes
turtle.fillcolor('red')
turtle.begin_fill() # Before drawing shape
# Draw shape (Circle as example)
turtle.begin_fill() # After drawing shape
turtle.end_fill()   # Shape will be filled with the current fill color after end_fill()

# Get Input with a Dialog Box
# If cancel is clicked, 'None'aka null is returned
age = turtle.numinput('window_title', 'prompt')
name = turtle.textinput('window_title', 'prompt')
# For numinput you can also specify a default, minimum, and maximum value
rank = turtle.numinput('window_title', 'prompt', default=10, minval=0, maxval=100)

# Use this to tell turtle to keep listening instead of ending the script instantly.
# turtle.done() starts Turtle's event loop, so the graphics window stays open until you close it yourself.
# turtle.mainloop() serves the same purpose.
turtle.done()