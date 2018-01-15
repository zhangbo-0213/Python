# -*- coding: cp936 -*-
sentence=raw_input('输入一段话：')
print '使用Split()进行分割'
liststr=sentence.split()
for s in liststr:
    print s
print '使用join连接，连接字符为“-”'
s='-'
print s.join(liststr)
