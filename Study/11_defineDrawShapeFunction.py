import turtle
def drawShape(sides,length):
    angle=360/sides
    for again in range(sides):
        turtle.forward(length)
        turtle.right(angle)
        print again
  

drawShape(6,20)
turtle.done()
