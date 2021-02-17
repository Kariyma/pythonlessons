import turtle
import turtlefun as tf


liza = turtle.Turtle()
liza.shape('turtle')
liza.color('white')
liza.speed(10)
liza.penup()
w = turtle.Screen()
w.bgcolor('green')
w.setup(1200, 800)

liza.hideturtle()
liza.setposition(-550, 0)
liza.showturtle()
liza.left(90)

liza.pendown()
radius = 80
number_spring_turn = 5

tf.arc(liza, radius, 270, 'right')
for i in range(number_spring_turn - 1):
    tf.arc(liza, 0.2*radius, 270, 'right')
    tf.arc(liza, radius, 270, 'right')

turtle.done()
