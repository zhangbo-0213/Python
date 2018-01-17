# -*- coding: cp936 -*-
filename=raw_input('请输入要保存的文件名.txt\n')
data=raw_input('请输入要保存的内容：\n')
f=open(filename,'w')
f.write(data)
f.close()
f2=open(filename)
data2=f2.read()
print '输入的内容是：\n'
print data2
f2.close()
