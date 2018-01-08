# -*- coding: cp936 -*-
import turtle
def DrawShape(sides,length):
    angle=360/sides
    for again in range(sides):
        turtle.forward(length)
        turtle.right(angle)

side=int(raw_input("请输入想要画的图形的边数："))
length=int(raw_input('请输入想要画的图形的边长：'))
DrawShape(side,length)
turtle.done()
