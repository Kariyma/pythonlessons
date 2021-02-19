import turtle
import numpy as np


def regular_polygons(number_side: int, len_side: float):
    """
    Draw polygon with number of side and length side
    :param number_side:
    :param len_side:
    :return:
    """
    turtle.pendown()
    for j in range(number_side):
        turtle.left(360 / number_side)
        turtle.forward(len_side)
    turtle.penup()


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


def stars(number_vertices: int, radius):
    angle_out = 360 / number_vertices
    angle_in = 180 - angle_out
    angle_star = 180 / number_vertices
    # angle_star = 180 - 720 / number_vertices
    # angle_star = (180 - angle_in) / 2
    angle_0 = angle_in - 2*angle_star
    angle_01 = 2*angle_in - 180
    length_side = radius * 2 * np.sin((angle_out / 2) * (np.pi / 180))
    length_star = (2*length_side**2 - 4*length_side*np.cos(angle_in))**0.5
    pdw = turtle.pen()['pendown']
    if not pdw:
        turtle.pendown()
    for i in range(number_vertices):
        turtle.right(180 - angle_star)
        turtle.forward(length_star)
    if not pdw:
        turtle.penup()


# regular_polygons(8, 50)
turtle.pensize(5)
stars(11, 100)
turtle.done()
