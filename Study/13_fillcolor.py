import turtle
def DrawShape(color,sides,length):
    angle=360/sides
    turtle.fillcolor(color)
    turtle.begin_fill()
    for again in range(sides):
        turtle.forward(length)
        turtle.right(angle)
    turtle.end_fill()

def MovePen(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

DrawShape('red',5,20)
MovePen(50,50)
DrawShape('blue',8,10)

MovePen(100,0)
turtle.fillcolor('gray')
turtle.begin_fill()
turtle.forward(20)
turtle.right(90)
turtle.forward(20)
turtle.end_fill()

MovePen(200,0)
turtle.color('yellow')
turtle.forward(20)
turtle.right(90)
turtle.forward(20)

turtle.done()
