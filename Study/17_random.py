# -*- coding: cp936 -*-
import random

print 'random.uniform(10,20)'           #输出范围内的随机小数
print random.uniform(10,20)      #17.749276658
print 'random.uniform(20,10)'  
print random.uniform(20,10)      #11.9747960764


print 'random.random()'              #输出0-1之间的随机小数
print random.random()             #0.849376425391

print 'random.range(0,10,2)'                      #输出指定递增的范围内(不包括上限)的随机整数
print random.randrange(0,10,2)    #(0,2,4,6,8) 6

print 'random.randint(0,5)'                  #输出范围内的整数，包括上下限
print random.randint(0,5)            #3

#设置随机种子，同一个随机种子下得到的随机值相同，通常在调用随机函数前设置随机种子
random.seed(10)
print 'Random number with seed 10:',random.random()

random.seed(10)
print 'Random number with seed 10:',random.random()

random.seed(10)
print 'Random number with seed 10:',random.random()
result=random.randint(0,100)
print 'Guess What I Think?'
answer=input()
while(answer!=result):
    if(answer>result):
        print '%d is too big,try a small one:' % answer
        answer=input()
    if(answer<result):
        print '%d is too small,try a big one:' % answer
        answer=input()
print 'you got it,result is  %d' % result


