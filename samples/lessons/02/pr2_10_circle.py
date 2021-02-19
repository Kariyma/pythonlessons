import turtle
import turtlefun as tf

turtle.speed(9)
turtle.color('red')
turtle.shape('classic')



for i in range(12):
    tf.circle(50)
    turtle.right(30)

turtle.dot(30, 'yellow')
turtle.hideturtle()

turtle.done()
