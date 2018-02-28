# -*- coding: utf-8 -*-
import os
#列表解析
list1=[1,3,4,6,9,12,23,34,38]
#获得list1中的偶数并构建成新的list
#使用传统方法：
list2=[]
for i in list1:
    if i%2==0:
        list2.append(i)

print list2

#使用列表解析
list3=[i for i in list1 if i%2==0]
print list3
#对元素的操作同样可以放在构建过程中，如对选出的偶数/2操作
list4=[i/2 for i in list1 if i%2==0]
print list4

print ';'.join([str(i) for i in range(1,100) if i%2==0&i%3==0&i%5==0])

print [x*x for x in range(1,11) if x%2==0]

#两层循环全排列
print [m+n for m in 'ABC' for n in 'XYZ']

#列出文件和目录
print [d for d in os.listdir('.')]

d={'x':'A','y':'B','z':'C'}
for key,value in d.items():
    print (key,'=',value)

#将字符串列表中的所有字符串变为小写
L=['Hello','World','Apple',557,34,'TENCENT']
print [s.lower() for s in L if isinstance(s,str)]
