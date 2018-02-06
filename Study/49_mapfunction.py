# -*- coding: utf-8 -*-
#对一个数列中的每个元素翻倍
list1=[1,2,3,4,5]
#1.使用列表解析
list2=[i*2 for i in list1]
print list2

#使用map函数
#map为Python自带函数，其作用是将某个函数的功能全部应用到某一个序列中
def double_func(x):
    return 2*x
list2=map(double_func,list1)
print list2

#与lambda表达式结合
list2=map(lambda x:2*x,list1)
print list2

#两个列表的元素相加
list3=[2,3,4,5,6]
list4=[4,5,6,7,8]
list5=map(lambda x,y:x+y,list3,list4)
print list5

#map 中的函数会从对应的列表中依次取出元素，
#作为参数使用，同样将结果以列表的形式返回。
#所以要注意的是，函数的参数个数要与 map 中提供的序列组数相同，
#即函数有几个参数，就得有几组数据。

lst_1 = [1,2,3,4,5,6]
lst_2 = [1,3,5,7,9,11]
lst_3 = map(None, lst_1)
print lst_3
lst_4 = map(None, lst_1, lst_2)
print lst_4
