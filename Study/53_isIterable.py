# -*- coding: utf-8 -*-
from collections import Iterable

#通过collections模块的iterable类型可以判断一个对象是否可以迭代
print(isinstance('abc',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance(123,Iterable))


#Python内置函数enumerate可以将列表list变成索引-元素对，在for循环中同时迭代索引和元素本身
for i,value in enumerate(['A','B','C']):
    print(i,value)

#使用迭代查找一个list中最小和最大的。并返回一个tuple
def FindMinAndMax(L):
    if len(L)==0:
        return (None,None)
    min=max=L[0]
    for x in L:
        if x<min:
            min=x
        else :
            max=x
    return (min,max)

L=[12,3,45,6,78]
result=FindMinAndMax(L)
print(result)
