import turtle
import turtlefun as tf
import numpy as np

turtle.speed(9)
turtle.color('red')
turtle.shape('classic')

turtle.left(90)
for i in range(10):
    for angle in [180, -180]:
        tf.circle(20+10*i)
        turtle.right(angle)


turtle.hideturtle()
turtle.done()
