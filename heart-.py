import turtle

turtle.bgcolor("black")
screen = turtle.Screen()
screen.title("Heart Shape")

heart_turtle = turtle.Turtle()
heart_turtle.shape("triangle")
heart_turtle.speed(1)
heart_turtle.color("red")

heart_turtle.begin_fill()

heart_turtle.penup()
heart_turtle.goto(0, -100)
heart_turtle.pendown()

heart_turtle.left(50)
heart_turtle.forward(133)
heart_turtle.circle(50, 200)

heart_turtle.right(140)

heart_turtle.circle(50, 200)
heart_turtle.forward(133)

heart_turtle.end_fill()

turtle.done()