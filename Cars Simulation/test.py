import turtle
from turtle import *
import math

RADIUS = 100
CURSOR_SIZE = 20

screen = Screen()
screen.colormode(255)

turtle = Turtle("circle", visible=False)
# turtle.speed('fastest')
turtle.penup()

turtle.fillcolor(200, 125, 200)
turtle.shapesize(RADIUS / CURSOR_SIZE)

turtle.stamp()




screen.exitonclick()