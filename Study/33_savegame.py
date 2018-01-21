# -*- coding: utf-8 -*-
from random import randint
try:
    f=open('savegamebyname.txt')
    file=f.readlines()
    dic={}
    for line in file:
        s=line.split(' ')
        dic[s[0]]=s[1:]
    f.close()
    print '文件已读取'
except:
    f=open('savegamebyname.txt','w')
    data=''
    f.write(data)
    f.close()
    print '文件已创建'
    f=open('savegamebyname.txt')
    file=f.readlines()
    dic={}
    for line in file:
        s=line.split(' ')
        dic[s[0]]=s[1:]
    f.close()


name=raw_input('请输入游戏玩家名字：')
score=dic.get(name)
if score is None:
    score=[0,0,0]
game_times=int(score[0])
min_time=int(score[1])
total_times=int(score[2])
if game_times==0:
    avg=0
else:
    avg=float(total_times)/game_times
print '%s 目前游戏的总次数： %d\n猜对的最小轮数: %d\n平均 %.2f轮猜对' % (name,game_times,min_time,avg)

bingo=False
num=randint(0,100)
min_times=0
print 'Guess What I Think'
while bingo!=True:
    min_times+=1
    answer=input()
    if answer<num:
        print 'Too Small'
    if answer>num:
        print 'Too Big'
    if answer==num:
        print 'Bingo'
        bingo=True
if min_time==0 or min_times<min_time:
    min_time=min_times
game_times+=1
total_times+=min_times
dic[name]=[str(game_times),str(min_time),str(total_times)]
result=''
for n in dic:
    line=n+' '+' '.join(dic[n])+'\n'
    result+=line
f=open('savegamebyname.txt','w')
f.write(result)
f.close()
avg=float(total_times)/game_times
print '数据已更新，%s目前游戏的总次数： %d\n猜对的最小轮数: %d\n平均 %.2f轮猜对' % (name,game_times,min_time,avg)

