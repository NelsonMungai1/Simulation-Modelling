import turtle
import random

def generate_random_color():
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    return color

car = turtle.Turtle()
car.speed(0)
car.screen.bgcolor("#fff")

def draw_Car(i, j, rand_hex_color):
    # Drawing the upper body
    car.fillcolor(rand_hex_color)
    car.penup()
    car.goto(i, j)
    car.pendown()
    car.begin_fill()
    car.forward(370)
    car.left(90)
    car.forward(50)
    car.left(90)
    car.forward(370)
    car.left(90)
    car.forward(50)
    car.end_fill()

    # Draw windows
    car.fillcolor("#D3D3D3")
    car.penup()
    car.goto(i + 100, 50)
    car.pendown()
    car.begin_fill()
    car.setheading(45)
    car.forward(70)
    car.setheading(0)
    car.forward(100)
    car.setheading(-45)
    car.forward(70)
    car.setheading(90)
    car.end_fill()
    car.penup()
    car.goto(i + 200, 50)
    car.pendown()
    car.forward(49.50)

    # Draw seats
    car.fillcolor("yellow")
    car.penup()
    car.goto(i + 150, 50)
    car.pendown()
    car.begin_fill()
    car.setheading(45)
    car.forward(40)
    car.setheading(0)
    car.forward(10)
    car.setheading(225)
    car.forward(40)

    car.penup()
    car.goto(i + 210, 50)
    car.pendown()
    car.setheading(45)
    car.forward(40)
    car.setheading(0)
    car.forward(10)
    car.setheading(225)
    car.forward(40)
    car.end_fill()

    # Draw the 2 wheels
    car.penup()
    car.goto(i + 100, 0)
    car.pendown()
    car.color("black")
    car.fillcolor("black")
    car.begin_fill()
    car.circle(20)
    car.end_fill()
    car.penup()
    car.goto(i + 300, 0)
    car.pendown()
    car.color("black")
    car.fillcolor("black")
    car.begin_fill()
    car.circle(20)
    car.end_fill()

    car.hideturtle()

rand_hex_color = generate_random_color()
draw_Car(-200, 0, rand_hex_color)
turtle.done()
