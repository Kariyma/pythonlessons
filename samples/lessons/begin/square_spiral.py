import turtle

turtle.shape('arrow')
turtle.speed(9)
turtle.color('red')

increment_length = 10
number_turns = 10
number_side_polygon = 3

side_length = increment_length
for i in range(number_turns):
    for j in range(number_side_polygon):
        turtle.forward(side_length)
        turtle.left(360 / number_side_polygon)
        side_length += increment_length

turtle.done()