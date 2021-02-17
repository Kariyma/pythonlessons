import turtle
import numpy as np


def hypotenuse_legs(leg1, leg2):
    return (leg1**2 + leg2**2)**0.5


def hypotenuse_leg_angle(leg1, angle_g):
    return leg1 / np.sin(angle_g*np.pi/180)


num_side_polygonal = int(input('Число сторон многоугольника '))
len_side_first_polygonal = int(input('Длина стороны многоугольника '))
num_polygonal = int(input('Число многоугольников '))
increment_angle = (180 - (360 / num_side_polygonal)) / 2
turtle.shape('turtle')
turtle.speed(1)

len_side_cur_polygonal = len_side_first_polygonal
for j in range(num_polygonal):
    for i in range(num_side_polygonal):
        turtle.left(360 / num_side_polygonal)
        turtle.forward(len_side_cur_polygonal)
    turtle.penup()
    turtle.right(increment_angle)
    turtle.forward(hypotenuse_leg_angle(len_side_first_polygonal, 360 / num_side_polygonal / 2))
    turtle.left(increment_angle)
    turtle.pendown()
    len_side_cur_polygonal += len_side_first_polygonal * 2
turtle.done()
