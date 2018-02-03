# -*- coding:utf-8 -*-
#lambda表达式
def sum(a,b,c):
    return a+b+c

print sum(1,2,3)

#这里sum1是一个函数对象
sum1=lambda a,b,c:a+b+c
print sum1(1,2,3)
