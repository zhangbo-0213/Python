# -*- coding: cp936 -*-
f=open('scores.txt')
lines=f.readlines()
f.close()
print '读取到的文件:\n'
results=[]
for line in lines:
    print line
for line in lines:
    datas=line.split()
    sums=0
    for data in datas[1:]:
        sums+=int(data)
    result=line+'%s\t:%d\n'%(datas[0],sums)
    results.append(result)

f2=open('output.txt','w')
f2.writelines(results)
f2.close()
print '处理后的文件：\n'
f3=open('output.txt')
data3=f3.read()
f3.close()
print data3
