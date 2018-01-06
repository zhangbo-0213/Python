import turtle
length=5
angle=20
circles=7
i=0
while i<circles*(360/angle):
    turtle.forward(length)
    turtle.right(angle)
    i+=1
    length+=1
turtle.done()
