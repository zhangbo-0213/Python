# -*- coding: cp936 -*-
try:
    f=open('non-exist.txt')
    print 'file open'
    f.close
except:
    print 'File not exists'
print 'Done'

#如果try内出现异常，执行except内的代码
#如果try内没有出现异常，执行try内的代码
#程序不会被中断，最后的 ‘Done' 会被输出
