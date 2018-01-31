# -*- coding: utf-8 -*-
import urllib2
from city2 import city
import json
cityname=raw_input('你想查询哪个城市的天气？\n')
citycode=city.get(cityname)
#print citycode
if citycode:
    url=('http://www.weather.com.cn/data/cityinfo/%s.html' % citycode)
    content=urllib2.urlopen(url).read()
    data=json.loads(content)
    result=data['weatherinfo']
    str_temp='%s %s~%s'%(result['weather'],result['temp1'],result['temp2'])
    print str_temp
else:
    print '没有找到该城市'
