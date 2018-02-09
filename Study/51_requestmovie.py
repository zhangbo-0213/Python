# -*- coding: utf-8 -*-
#通过豆瓣API抓取影片信息

import urllib,time

time_start=time.time()
data=[]
for i in range(30):
    print 'request movie:',i
    id=1764796+i
    url='https://api.douban.com/v2/movie/subject/%d'% id
    d=urllib.urlopen(url).read()
    data.append(d)
    print i,time.time()-time_start

print 'data',len(data)
