# -*- coding:utf-8 -*-
import http.cookiejar
import socket
import urllib.request
import urllib.parse
import urllib.error
from urllib import parse, request

#urllib.request相关使用

#获取网页请求(GET请求)
response=urllib.request.urlopen('http://www.baidu.com')
print(response.read().decode('utf-8'))
#response.read()获取响应体的内容，是bytes字节流形式，因此需要进行编码

#提交网页请求(POST请求)
#POST请求需要传入额外信息
data=bytes(urllib.parse.urlencode({'world':'hello'}),encoding='utf-8')
response=urllib.request.urlopen('http://httpbin.org/post',data=data)
print(response.read())

#设置请求超时时间，若超时时间内没有得到响应，则会抛出异常
data=bytes(urllib.parse.urlencode({'world':'hello'}),encoding='utf-8')
response=urllib.request.urlopen('http://httpbin.org/post',data=data,timeout=1)
print(response.read())

try:
    data=bytes(urllib.parse.urlencode({'world':'hello'}),encoding='utf-8')
    response=urllib.request.urlopen('http://httpbin.org/post',data=data,timeout=0.1)
    print(response.read())
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('TIME OUT')

#响应类型
response=urllib.request.urlopen('http://www.baidu.com')
print(type(response))

#状态码，响应头的获取
response=urllib.request.urlopen('http://www.baidu.com')
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))

#使用request.Request构造request对象，通过urlopen发送请求
url='http://httpbin.org/post'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Host':'httpbin.org'
}
dic={'name':'MajorTom'}
data=bytes(parse.urlencode(dic),encoding='utf-8')
req=request.Request(url=url,data=data,headers=headers,method='POST')
response=request.urlopen(req)
print(response.read().decode('utf-8'))

'''
#Handler相关使用

#构建proxy handler代理工具
#通过构建代理设置访问的IP地址来避免目标网页的反爬虫设置
proxy_handler=urllib.request.ProxyHandler({
    'http':'115.223.234.172:9000'
})
#通过urllib.request.build_opener()方法使用代理对象，创建自定义opener对象
opener=urllib.request.build_opener(proxy_handler)
#使用自定义opener.open()方法发送请求才能使用自定义代理，而urlopen()则不使用代理
response=opener.open('http://httpbin.org/get')
print(response.read().decode('utf-8'))
'''

#Cookies:
# 在 Internet 中，Cookie 实际上是指小量信息，是由 Web 服务器创建的，
# 将信息存储在用户计算机上的文件。一般网络用户习惯用其复数形式 Cookies，
# 指某些网站为了辨别用户身份、进行 Session 跟踪而存储在用户本地终端上的数据，
# 而这些数据通常会经过加密处理
# Cookie是用来维持登录状态的机制，记录用户身份

#Cookie获取
#构建cookie容器
cookie=http.cookiejar.CookieJar()
#构建Cookie代理对象
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
response=opener.open('http://www.baidu.com')
#当请求成功后，cookie会被目标站点创建内容并赋值
for item in cookie:
    print(item.name+"="+item.value)

#保存cookie到本地内容
filename='cookie.txt'
#MozillaCookieJar()为CookieJar()的子类，构建子类对象，使用其save方法保存cookies
cookie=http.cookiejar.MozillaCookieJar(filename)
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
response=opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True,ignore_expires=True)

#读取cookies文件，并构建request对象发送请求
cookies=http.cookiejar.MozillaCookieJar()
cookies.load('cookie.txt',ignore_discard=True,ignore_expires=True)
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
response=opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))

#cookies对象有不同种类，例如http.cookiejar.LWPCookieJar()，
#在保存和加载cookies对象时，使用对应的种类即可


#异常处理
#urllib库中提供了关于异常处理的类
#父类  URLError  只提供了 reason的属性
#子类  HTTPError 提供 code reason headers属性
try:
    response=request.urlopen('http://majortom.com/index.htm')
#先捕获子类异常
except urllib.error.HTTPError as e:
    print(e.code,e.reason,e.headers,sep='\n')
except urllib.error.URLError as e:
    print(e.reason)
else:
    print('Request Successfully')

try:
    response=request.urlopen('http://www.baidu.com',timeout=0.01)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('TIME OUT')

#URL解析
#urllib.parse 工具模块，提供URL解析的方法

#urlparse()方法 拆分url
result=urllib.parse.urlparse('https://www.baidu.com/index.html;user?id=5#comment')
print(type(result),result)
#输出：<class 'urllib.parse.ParseResult'>
#ParseResult(scheme='https', netloc='www.baidu.com', path='/index.html', params='user', query='id=5', fragment='comment')
#(协议类型，域名，路径，参数，查找元素，片段)

#当没有协议类型，通过urlparse方法可以传入协议类型
result=urllib.parse.urlparse('www.baidu.com/index.html;user?id=5#comment',scheme='https')
print(result)
#输出ParseResult(scheme='https', netloc='', path='www.baidu.com/index.html', params='user', query='id=5', fragment='comment')
#当链接中给定了协议类型，以给定的协议类型为主

#parse.urlunparse()方法   url拼接
data=['http','www.baidu.com','index.html','uesr','a=6','comment']
print(parse.urlunparse(data))
#输出
#http://www.baidu.com/index.html;uesr?a=6#comment

#parse.urljoin()
#urljoin()方法 参数叠加生成url,叠加过程有一定的规则
#（以第二个参数中的url的6个字段为准，如果第二个参数中的6个字段对应存在则覆盖第一个的，
# 不存在则以第一个参数字段作为补充，然后整体返回结果中）
print(parse.urljoin('http://www.baidu.com','FAQ.html'))
print(parse.urljoin('http://www.baidu.com','https://cuiqingcai.com/FAQ.html'))
print(parse.urljoin('http://www.baidu.com/about.html','https://cuiqingcai.com/FAQ.html'))
print(parse.urljoin('http://www.baidu.com/about.html','https://cuiqingcai.com/FAQ.html？question=2'))
print(parse.urljoin('http://www.baidu.com/?wd=abc','https://cuiqingcai.com/index.php'))
print(parse.urljoin('http://www.baidu.com','?catagory=2#comment'))
print(parse.urljoin('www.baidu.com','?catagory=2#comment'))
print(parse.urljoin('www.baidu.com#comment','?catagory=2'))

#输出
#http://www.baidu.com/FAQ.html
#https://cuiqingcai.com/FAQ.html
#https://cuiqingcai.com/FAQ.html
#https://cuiqingcai.com/FAQ.html？question=2
#https://cuiqingcai.com/index.php
#http://www.baidu.com?catagory=2#comment
#www.baidu.com?catagory=2#comment
#www.baidu.com?catagory=2


#urlencode()方法   将字典形式存储的url字段参数转化为url请求参数
params={
    'name':'majortom',
    'age':22
}
base_url='http://www.baidu.com?'
url=base_url+parse.urlencode(params)
print(url)
#输出
#http://www.baidu.com?name=majortom&age=22
