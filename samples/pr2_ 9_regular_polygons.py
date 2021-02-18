import turtle
import numpy as np
import turtlefun as tf


def main():
    turtle.shape('classic')
    turtle.speed(9)
    turtle.color('green')
    turtle.penup()

    step_polygonal = 20
    number_polygonal = 10
    start_number_side_polygonal = 3
    radius = 0

    turtle.left(90)
    for n in range(start_number_side_polygonal, number_polygonal + start_number_side_polygonal, 1):
        angle_1 = 360/n
        angle_2 = (180 - angle_1)/2
        radius += step_polygonal
        length = radius*2*np.sin((angle_1/2)*(np.pi/180))
        turtle.forward(step_polygonal)
        turtle.left(angle_2)

        tf.regular_polygons(n, length)

        turtle.right(angle_2)

    turtle.done()


if __name__ == '__main__':
    main()
