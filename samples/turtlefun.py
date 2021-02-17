import turtle
import numpy as np


def circle(radius):
    number_side_polygon = 100
    angle = 360 / number_side_polygon
    length_side = radius*2*np.sin((angle/2)*(np.pi/180))
    pdw = turtle.pen()['pendown']
    if not pdw:
        turtle.pendown()
    for i in range(number_side_polygon):
        turtle.left(angle)
        turtle.forward(length_side)
    if not pdw:
        turtle.penup()


def arc(tr, radius=100, angel=180, direction='left'):
    number_side_polygon = 100
    angle = angel / number_side_polygon
    length_side = radius*2*np.sin((angle/2)*(np.pi/180))
    pdw = turtle.pen()['pendown']
    if not pdw:
        turtle.pendown()
    for i in range(number_side_polygon):
        if direction == 'right':
            tr.right(angle)
        else:
            tr.left(angle)
        tr.forward(length_side)
    if not pdw:
        turtle.penup()
