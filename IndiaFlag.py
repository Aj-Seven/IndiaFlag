import turtle
t = turtle.Turtle()
turtle.bgcolor('black')
turtle.title("India Flag")
t.hideturtle()
for i in range(1):
    t.speed(8)
    t.pencolor('red')
    t.penup()
    t.setpos(-90, 250)
    t.pendown()
    t.begin_fill()
    t.color('orange')
    t.pencolor('orange')
    t.fd(200)
    t.right(90)
    t.fd(50)
    t.right(90)
    t.fd(200)
    t.right(90)
    t.fd(50)
    t.right(90)
    t.end_fill()
    t.penup()
    t.setpos(-90, 200)
    t.right(90)
    t.pendown()
    t.begin_fill()
    t.color('white')
    t.pencolor('white')
    t.fd(50)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(50)
    t.end_fill()
    t.penup()
    t.setpos(-90, 150)
    t.pendown()
    t.begin_fill()
    t.color('green')
    t.pencolor('green')
    t.right(90)
    t.right(90)
    t.fd(50)
    t.left(90)
    t.fd(200)
    t.left(90)
    t.fd(50)
    t.end_fill()
    t.penup()
    t.pencolor('gray')
    t.setpos(-90, 100)
    t.right(90)
    t.right(90)
    t.pendown()
    t.pensize(3)
    t.pencolor('brown')
    t.fd(240)
    t.color('red')
    t.pencolor('red')
    t.begin_fill()
    t.pensize(0)
    t.left(90)
    t.fd(80)
    t.right(90)
    t.fd(30)
    t.right(90)
    t.fd(160)
    t.right(90)
    t.fd(30)
    t.right(90)
    t.fd(90)
    t.penup()
    t.setpos(-10, -170)
    t.pendown()
    t.forward(80)
    t.right(90)
    t.fd(30)
    t.right(90)
    t.forward(330)
    t.right(90)
    t.fd(30)
    t.right(90)
    t.fd(320)
    t.right(90)
    t.fd(30)
    t.left(90)
    t.fd(80)
    t.right(90)
    t.fd(30)
    t.right(90)
    t.fd(460)
    t.right(90)
    t.fd(30)
    t.right(90)
    t.fd(80)
    t.end_fill()
    t.penup()
    t.goto(10,150)
    t.pendown()
    t.pencolor('blue')
    t.pensize(1.4)
    t.circle(25.5)
    t.penup()
    t.goto(10,178)
    t.hideturtle()
for i in range(24):
    t.pendown()
    t.goto(10, 176)
    t.pencolor('blue')
    t.color('blue')
    t.begin_fill()
    t.fd(24.5)
    t.left(15)
    t.backward(20)
    t.end_fill()
    t.penup()
turtle.color('skyblue')
turtle.penup()
turtle.hideturtle()
turtle.goto(90,-280)
turtle.pendown()
turtle.write(arg = "==>Made by Aj7", font=("Verdana",7,"bold"))
turtle.hideturtle()
turtle.done()
