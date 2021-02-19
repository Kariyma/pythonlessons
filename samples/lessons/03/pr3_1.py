from random import *
import turtle

turtle.Screen().setup(800, 800)
turtle.shape('classic')
turtle.color('yellow')
turtle.pencolor('red')
turtle.speed(10)
turtle.pensize(3)

while (True):
    turtle.stamp()
    turtle.right(randint(-360, 360))
    turtle.forward(random()*100)

