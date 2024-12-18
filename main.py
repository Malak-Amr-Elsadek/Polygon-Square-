import turtle
turtle.Screen().bgcolor("Hot pink")
turtle.Screen().setup(300,400)

pen =turtle.Turtle()
pen.color("violet")
pen.width(10)

for i in range(4):
    pen.forward(100)
    pen.right(90)

turtle.done()