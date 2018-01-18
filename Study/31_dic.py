# -*- coding: cp936 -*-
dic={'炸弹人':'法师','火男':'法师','奥巴马':'ADC','盲僧':'打野'}
print '输出字典内容：'
for hero in dic:
    print hero+': '+dic[hero]
print r'添加字典成员：皇子：打野'
dic['皇子']="打野"
print '输出字典内容：'
for hero in dic:
    print hero+': '+dic[hero]   
print r'删除字典成员：盲僧：打野'
del dic['盲僧']
print '输出字典内容：'
for hero in dic:
    print hero+': '+dic[hero]
