import turtle
import turtlefun as tf

turtle.shape('turtle')
turtle.speed(10)
turtle.Screen().setup(1200, 800)

radius = int(input('Радиус описанной окружности: '))
stars_vertices = int(input('Количество вершин звезды: '))

turtle.pencolor('red')
turtle.penup()
turtle.setposition(-100, 50)
tf.stars(stars_vertices, radius)
turtle.done()
