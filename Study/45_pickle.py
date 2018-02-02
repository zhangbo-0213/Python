# -*- coding:utf-8 -*-
#pickle 用于序列化和反序列化操作
#序列化：将对象转化成可保持或传输的格式的过程
#反序列化：从序列化的格式中解析出对象的过程

import pickle
test_data=["Save me",123.45,True]
f=file('pickleTest.data','w')
#序列化存储
pickle.dump(test_data,f)
f.close()

f=file('pickleTest.data')
#序列化提取
test_data=pickle.load(f)
f.close()
print test_data
