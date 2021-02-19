from random import *
import turtle

turtle.Screen().setup(800, 800)
turtle.shape('classic')
turtle.color('yellow')
# turtle.color('#285078')
turtle.pencolor('red')
turtle.speed(10)
turtle.pensize(3)

color = ['red', 'black', 'green', 'yellow', 'blue']

while (True):
    turtle.stamp()
    turtle.right(randint(-360, 360))
    turtle.forward(random()*100)
    # turtle.color(color[randint(0, 4)])
    # turtle.pencolor(color[randint(0, 4)])
    tc = '#'
    pc = '#'
    for j in range(6):
        tc += str(randint(0,9))
        pc += str(randint(0,6))
    turtle.color(tc)
    turtle.pencolor(pc)
