import turtle
import numpy as np

num_side_polygonal = 120
len_side_first_polygonal = 10
increment_spiral_length = 10
increment_spiral_angle = 0.05
increment_spiral = increment_spiral_length / (2*np.pi)
increment_spiral_radius = increment_spiral * increment_spiral_angle
angle = np.arange(0, 50, increment_spiral_angle)

turtle.speed(9)
turtle.shape('classic')

for i in angle:
    dl = increment_spiral * increment_spiral_angle * (1 + i**2)**0.5
    turn_angle = increment_spiral_angle*180/np.pi
    turtle.forward(dl)
    turtle.left(turn_angle)

turtle.done()
