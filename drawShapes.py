from turtle import *
import math

def drawShape(t, sides):
    #Draws shapes (circle=1)
    if sides > 1:
        for x in range(sides):
            t.forward(100/(sides/5))
            t.left(360/sides)
    else:
        t.circle(100)

def main():
    # Name your Turtle.
    t = Turtle()

    #User input for color and number of sides
    color = input ('Enter a color: ')
    t.pencolor(color)

    sides = int (input ('Enter number of sides: '))

    # Set Up your screen and starting position.
    setup(500,300)
    t.penup()
    t.setposition(-100,-100)
    t.pendown()

    drawShape(t, sides)

    # Close window on click.
    exitonclick()

main()
