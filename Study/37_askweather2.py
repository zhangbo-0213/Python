# -*- coding: utf-8 -*-
import urllib2
result='city={\n'
#抓取省份列表
url1='http://m.weather.com.cn/data3/city.xml'
content=urllib2.urlopen(url1).read()
provinces=content.split(',')

#对于每个省抓取城市列表
url='http://m.weather.com.cn/data3/city%s.xml'
for p in provinces:
    p_code=p.split('|')[0]
    url2=url % p_code
    content2=urllib2.urlopen(url2).read()
    citys=content2.split(',')
#    for city in citys:
#       print city
#对于每个城市抓取地区
    for c in citys:
        c_code=c.split('|')[0]
        url3=url % c_code
        content3=urllib2.urlopen(url3).read()
        zones=content3.split(',')
#        for zone in zones:
#            print zone
#对于每个地区访问完整的地区编码
        for zone in zones[:]:
            z_pair=zone.split('|')
            z_code=z_pair[0]
            z_name=z_pair[1]
            url4=url % z_code
            content4=urllib2.urlopen(url4).read()
            code=content4.split('|')[1]
            line="  '%s':'%s',\n" % (z_name,code)
            result+=line
            print z_name+':'+code

result+='}'
f=open('city2.py','w')
f.write(result)
f.close()


