import turtle
def DrawShape(sides,length):
    angle=360/sides
    for again in range(sides):
        turtle.forward(length)
        turtle.right(angle)

def DrawCircle(length):
    DrawShape(360,length)

turtle.color('red')
turtle.fillcolor('blue')
turtle.begin_fill()
DrawCircle(2)
turtle.end_fill()
turtle.done()

