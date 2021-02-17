import turtle
import numpy as np


def circle(radius):
    number_side_polygon = 100
    angle = 360 / number_side_polygon
    length_side = radius*2*np.sin((angle/2)*(np.pi/180))
    for i in range(number_side_polygon):
        turtle.left(angle)
        turtle.forward(length_side)

