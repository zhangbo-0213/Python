# -*- coding:utf-8 -*-
#参数的多种传递方式
def func(x,y=5,*args,**krgs):
    print x,y,args,krgs

func(3)
func(3,4)
func(3,4,5)
func(3,4,5,8)
func(x=1)
func(x=1,y=1)
func(x=1,y=1,a=1)
func(x=1,y=1,a=1,b=1)
func(1,y=1)
func(1,2,3,4,a=1)
func(1,2,3,4,a=1,b=2,c=3,k=4)
