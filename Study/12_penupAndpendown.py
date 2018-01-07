import turtle
def drawShape(sides,length):
    angle=360/sides
    for again in range(sides):
        turtle.forward(length)
        turtle.right(angle)
        print again

def MovePen(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

drawShape(6,20)
MovePen(50,0)
drawShape(8,10)
turtle.done()
