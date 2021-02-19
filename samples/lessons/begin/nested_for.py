import turtle


def david():
    turtle.pendown()
    for step in range(6):
        turtle.begin_fill()
        for i in range(3):
            turtle.forward(100)
            turtle.left(120)
        turtle.end_fill()
        turtle.forward(100)
        turtle.right(60)


turtle.shape('turtle')
turtle.shapesize(2)
turtle.color('red', 'yellow')
turtle.speed(50)
turtle.penup()
turtle.goto(-200, 250)

for out in range(6):
    david()
    turtle.penup()
    turtle.forward(300)
    turtle.right(60)

turtle.hideturtle()

turtle.done()
# turtle.mainloop()
