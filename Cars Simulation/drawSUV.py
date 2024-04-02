import turtle
import random

def generate_random_color():
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    return color


def draw_car(i, j, rand_hex_color, scale):
    # Draw car at specified position with specified scale
    car = turtle.Turtle()
    car.speed("fastest")
    # upper body 
    car.color("grey")
    car.fillcolor(rand_hex_color)
    car.penup()
    car.goto(i*scale,j*scale)
    car.pendown()
    car.begin_fill()
    car.forward(400*scale)
    car.left(90)
    car.forward(100*scale)
    car.left(90)
    car.forward(400*scale)
    car.left(90)
    car.forward(100*scale)
    car.end_fill()

    # door
    car.penup()
    car.goto((i+100)*scale,100*scale)
    car.pendown()
    car.setheading(40)
    car.forward(125*scale)
    car.setheading(0)
    car.forward(200*scale)
    car.setheading(-90)
    car.forward(80*scale)
    car.setheading(90)
    car.penup()
    car.goto(200*scale,50*scale)
    car.pendown()
    car.forward(49.5*scale)
    
    # windows
    car.penup()
    car.goto((i+200)*scale,100*scale)
    car.pendown()
    car.setheading(90)
    car.forward(79*scale)

    car.penup()
    car.goto((i+300)*scale,100*scale)
    car.pendown()
    car.setheading(90)
    car.forward(79*scale)

    # Seats
    # car.fillcolor("#F5F5DC")
    # car.begin_fill()
    # car.penup()
    # car.goto(i+0,100)    
    # car.pendown()
    # car.setheading(45)
    # car.forward(70)
    # car.setheading(0)
    # car.forward(10)
    # car.setheading(225)
    # car.forward(70)
    # car.end_fill()

    car.fillcolor("#F5F5DC")
    car.begin_fill()
    car.penup()
    car.goto((i+230)*scale,100*scale)    
    car.pendown()
    car.setheading(45)
    car.forward(70*scale)
    car.setheading(0)
    car.forward(10*scale)
    car.setheading(225)
    car.forward(70*scale)
    car.end_fill()

    car.fillcolor("#F5F5DC")
    car.begin_fill()
    car.penup()
    car.goto((i+300)*scale,100*scale)    
    car.pendown()
    car.setheading(45)
    car.forward(70*scale)
    car.setheading(0)
    car.forward(10*scale)
    car.setheading(225)
    car.forward(70*scale)
    car.end_fill()

    # wheels 
    car.penup()
    car.goto((200)*scale,150*scale)
    car.pendown()
    car.color("black")
    car.fillcolor("black")
    car.begin_fill()
    car.circle(30*scale)
    car.end_fill()
    car.penup()
    car.goto((-100)*scale,-10*scale)
    car.pendown()
    car.color("black")
    car.fillcolor("black")
    car.begin_fill()
    car.circle(30*scale)
    car.end_fill()

    car.penup()
    car.goto(100*scale,-10*scale)
    car.pendown()
    car.color("black")
    car.fillcolor("black")
    car.begin_fill()
    car.circle(30*scale)
    car.end_fill()
    car.hideturtle()
    # turtle.done()
    turtle.update()

rand_hex_color=generate_random_color()
# draw_car(-200,0,rand_hex_color)
# scale=random.uniform(0.1,0.3)
def main(): 
    turtle.title("SUV")
    turtle.tracer(0,0)#disable animation

    scale=random.uniform(0.1,1.5)
    draw_car(-200,0,rand_hex_color,scale)

    turtle.update()
    turtle.done()


if __name__=="__main__":
    main()