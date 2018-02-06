# -*- coding: utf-8 -*-
#ruduce函数则是将某个规则应用到列表中的元素，
#并将所得结果与下一下元素继续应用规则，
#直到应用到列表的最后一个元素，最后得到输出。

#求一个数列的和
list1=range(1,101)
def add(x,y):
    return x+y

sum1=reduce(add,list1)
print sum1

#使用lambda表达式
sum2=reduce(lambda x,y:x+y,range(1,101))
print sum2
