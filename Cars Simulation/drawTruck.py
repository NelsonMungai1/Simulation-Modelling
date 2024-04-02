import turtle
import random

def generate_random_color():
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    return color

car=turtle.Turtle()
car.speed("fastest")

turtle.title("SUV")
turtle.tracer(0,0)#disable animation
def draw_lorry(i, j, rand_hex_color):
    # Main body
    car.color("grey")
    car.fillcolor(rand_hex_color)
    car.penup()
    car.goto(i, j)
    car.pendown()
    car.begin_fill()
    car.forward(400)
    car.left(90)
    car.forward(150)
    car.left(90)
    car.forward(400)
    car.left(90)
    car.forward(150)
    car.end_fill()

    # Cabin
    car.penup()
    car.goto(i + 400,100)
    car.pendown()
    car.fillcolor("Grey")
    car.begin_fill()
    car.setheading(0)
    car.forward(70)
    car.setheading(-45)
    car.forward(40)
    car.setheading(-90)
    car.forward(70)
    car.left(-90)
    car.forward(100)
    car.end_fill()

    # window
    car.penup()
    car.goto(i + 400,100)
    car.pendown()
    car.fillcolor("white")
    car.begin_fill()
    car.setheading(0)
    car.forward(70)
    car.setheading(-45)
    car.forward(40)
    car.setheading(-180)
    car.forward(100)
    car.penup()
    car.goto(i+440,100)
    car.pendown()
    car.setheading(-90)
    car.forward(30)
    car.end_fill()

    # Wheels
    car.penup()
    car.goto(i + 50,j-30) 
    car.pendown()
    car.color("black")
    car.fillcolor("black")
    car.begin_fill()
    car.circle(40)
    car.end_fill()

    car.penup()
    car.goto(i + 430, j-30)
    car.pendown()
    car.color("black")
    car.fillcolor("black")
    car.begin_fill()
    car.circle(40)
    car.end_fill()

    car.hideturtle()
    turtle.done()
    turtle.update()

# Usage

rand_hex_color = generate_random_color()
draw_lorry(-300, 0, rand_hex_color)
