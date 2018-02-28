# -*- coding:utf-8 -*-

#创建生成器的方法一，将列表解析中的[]改为()
L=(x*x for x in range(6))
#生成器的元素通过next（）函数得到
print next(L)
print next(L)
print next(L)
print next(L)
print next(L)
print next(L)
#生成器保存算法，每次调用next（）函数得到下一个元素的值，直到最后一个元素，没有更多元素时
#抛出StopIteration错误
#生成器也属于可迭代对象，可以通过for进行遍历
g=(2*x for x in range(10))
for n in g:
    print n

#创建生成器的方法二，使用yield关键字

#打印斐波那契数列的函数
def fbb(max):
    n,a,b=0,0,1
    while n<max:
        print b
        a,b=b,a+b
        n=n+1
    return 'done'
print fbb(6)

#如果想要保存斐波那契数列结果，一般做法需要通过列表保存下来
def fbb2(max):
    L=[]
    n,a,b=0,0,1
    while n<max:
        L.append(b)
        a,b=b,a+b
        n=n+1
    return L

print [x for x in fbb2(6)]

#而当这个数列需要返回的元素个数很多时，使用列表就会占用大量的空间，因此这里使用yield
#yield使普通函数作为一个生成器，每次只返回当前迭代的元素结果
def fbb3(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1

#普通函数是顺序执行，而generator生成器是在调用next（）执行，遇到yield返回，yield后的结果，
#再次遇到next（）继续上一次的进行，直到没有更多元素，抛StopIteration异常结束
#生成器可迭代，因此通过for循环自动执行next()直到结束，不会抛出StopIteration异常
for x in fbb3(10):
    print x

#计算杨辉三角
def YangAngles():
    L=[1]
    while True:
        yield L
        L=[1]+[L[n]+L[n+1] for n in range(len(L)-1)]+[1]

i=0
for n in YangAngles():
    print(n)
    i=i+1
    if i==10:
        break


