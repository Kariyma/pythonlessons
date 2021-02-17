import turtle

paw_length = 100
paw_number = 12

turtle.shape('turtle')
turtle.color('red')
turtle.speed(9)

for i in range(paw_number):
    turtle.forward(paw_length)
    turtle.stamp()
    turtle.left(180)
    turtle.forward(paw_length)
    turtle.right(180 - 360 / paw_number)

turtle.done()

