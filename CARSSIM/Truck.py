import turtle
car=turtle.Turtle()

car.color("grey")
car.fillcolor("black")
car.penup()
car.goto(-200,0)
car.pendown()
car.begin_fill()
car.forward(400)
car.left(90)
car.forward(100)
car.left(90)
car.forward(400)
car.left(90)
car.forward(100)
car.end_fill()

car.penup()
car.goto(-100,100)
car.pendown()
car.setheading(35)
car.forward(125)
car.setheading(0)
car.forward(190)
car.setheading(-90)
car.forward(75)
car.setheading(90)
car.penup()
car.goto(200,50)
car.pendown()
car.forward(49.5)

car.penup()
car.goto(230,125)
car.pendown()
car.color("black")
car.fillcolor("black")
car.begin_fill()
car.circle(20)
car.end_fill()

car.penup()
car.goto(-100,-10)
car.pendown()
car.color("black")
car.fillcolor("black")
car.begin_fill()
car.circle(20)
car.end_fill()

car.penup()
car.goto(100,-10)
car.pendown()
car.color("black")
car.fillcolor("black")
car.begin_fill()
car.circle(20)
car.end_fill()
car.hideturtle()
turtle.done()
