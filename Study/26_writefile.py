# -*- coding: cp936 -*-
filename=raw_input('请输入要保存的文件名.txt\n')
print 'DataTest文件的内容是：'
f=open('DataTest.txt')
data=f.read()
print data
f.close()
f2=open(filename,'w')
f2.write(data)
f2.close()
print '将DataTest文件内容存入要保存文件后，文件内容是：\n'
f3=open(filename)
data2=f3.read()
print data2
f3.close()
