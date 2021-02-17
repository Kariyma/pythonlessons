import turtle
import numpy as np


def circle(radius):
    number_side_polygon = 100
    angle = 360 / number_side_polygon
    length_side = radius*2*np.sin((angle/2)*(np.pi/180))
    turtle.penup()
    turtle.forward(radius)
    turtle.pendown()
    for i in range(number_side_polygon):
        turtle.left(angle)
        turtle.forward(length_side)
    turtle.penup()
