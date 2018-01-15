# -*- coding: cp936 -*-
print 'Split() 默认将字符串进行分割'
sentence=raw_input('输入一段话：')
print '使用Split()得到：'
for s in sentence.split(','):
    print s+' ',
    
