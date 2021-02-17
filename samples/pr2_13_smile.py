import turtle
import turtlefun as tf

turtle.shape('turtle')
turtle.speed(9)
turtle.Screen().setup(1000, 1000)

turtle.penup()
turtle.setposition(0, -350)


turtle.fillcolor('yellow')
turtle.begin_fill()
tf.circle(400)
turtle.end_fill()

turtle.penup()
turtle.setposition(-180, 130)
turtle.fillcolor('blue')
turtle.begin_fill()
tf.circle(55)
turtle.setposition(180, 130)
tf.circle(55)
turtle.end_fill()

turtle.pensize(30)
turtle.setposition(0, 100)
turtle.pencolor('black')
turtle.right(90)
turtle.pendown()
turtle.forward(100)

turtle.penup()
turtle.pensize(40)
turtle.setposition(210, -100)
turtle.pencolor('red')
turtle.right(30)
tf.arc(turtle, 250, 120, 'right')


turtle.hideturtle()
turtle.done()