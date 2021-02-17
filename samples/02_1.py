import turtle

turtle.shape('turtle')
turtle.shapesize(3)
turtle.color('red')

a = [(100, 0), (200, 30), (50, 60), (100, 160)]
for length, angle in a:
    turtle.left(angle)
    turtle.forward(length)


turtle.done()