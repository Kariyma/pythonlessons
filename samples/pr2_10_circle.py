import turtle
import turtlefun as tf

turtle.speed(9)
turtle.color('blue')
turtle.shape('classic')

for i in range(6):
    tf.circle(100)
    turtle.right(60)

turtle.done()
