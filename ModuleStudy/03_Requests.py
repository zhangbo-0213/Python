# -*- coding: utf-8 -*-
#Requests库是使用Python编写,基于Urllib,比Urllib使用更加方便的HTTP第三方库

import requests
import json
from requests import Timeout, ReadTimeout,ConnectionError,RequestException

#实例引入
response=requests.get('http://www.baidu.com/')
print(type(response))
print(response.status_code)
print(type(response.text))
print(response.text)
print(response.cookies)

#各种请求方式
#使用 http://httpbin.org 进行测试
requests.post('http://httpbin.org/post')
requests.put('http://httpbin.org/put')
requests.delete('http://httpbin.org/delete')
requests.head('http://httpbin.org/get')
requests.options('http://httpbin.org/get')

#基本Get请求
response=requests.get('http://httpbin.org')
print(response.text)

#带参数的Get请求
data={
    'user':'majortom',
    'age':24
}
response=requests.get('http://httpbin.org/get',params=data)
print(response.text)

#josn解析
response=requests.get('http://httpbin.org/get')
print(type(response.text))
print(response.json())
print(json.loads(response.text))
print(type(response.json()))

#获取二进制数据(下载图片，视频信息时常用)
#response.content
response=requests.get('https://github.com/favicon.ico')
print(type(response.text))
print(response.text)
print(type(response.content))
print(response.content)
#下载保存图片
response=requests.get('http://github.com/favicon.ico')
with open('favicon.ico','wb+') as f:
    f.write(response.content)
    f.close()
print('下载完成')

#添加Headers（实现对浏览器的伪装）
#在爬虫中，如果对目标站点发起请求时，不添加任何信息，可能会被拒绝访问
#例如：
response=requests.get('http://www.zhihu.com/explore')
print(response.text)
#输出：
#<html><body><h1>500 Server Error</h1>
#An internal server error occured.
#</body></html>

#添加headers
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
         }
response=requests.get('http://www.zhihu.com/explore',headers=headers)
print(response.text)
#正常获取知乎发现页面的html内容

#基本POST请求
#Post请求需要在发出请求时提交表单(form-data)信息
data={'name':'MajorTom',
      'age':25}
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}
response=requests.post('http://httpbin.org/post',data=data,headers=headers)
print(response.text)

#响应
#response属性
response=requests.get('http://www.jianshu.com')
print(type(response.status_code),response.status_code)
print(type(response.headers),response.headers)
print(type(response.cookies),response.cookies)
print(type(response.url),response.url)
print(type(response.history),response.history)
#状态码判断
response=requests.get('http://www.jianshu.com')
exit() if not response.status_code==200 else print('Request Successfully')

#Requests高级操作
#文件上传
file={'file':open('favicon.ico','rb')}
#通过字典保存需要上传的文件
response=requests.post('http://httpbin.org/post',files=file)
print(response.text)

#获取cookie
response=requests.get('http://www.baidu.com')
print(response.cookies)
print(type(response.cookies.items()))
for key,values in response.cookies.items():
    print(key+'='+values)

#会话维持
#设置cookies,模拟登陆过程

requests.get('http://httpbin.org/cookies/set/number/123456789')
#使用httpbin/cookies/set 设置cookies信息
response=requests.get('http://httpbin.org/cookies')
#拿到当前请求的cookies
print(response.text)
#输出结果：  "cookies": {}
#cookies为空,这是由于两次get请求是相互独立的，相当于使用一个浏览器访问一个cookies，
#使用另外一个浏览器再去获取cookies,因此获取不到cookies信息

#如何模拟使用一个浏览器去设置cookies,再去获取cookies信息？
#使用Session对象，再用Session对象发起两次请求，分别设置和获取cookies
s=requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
response=s.get('http://httpbin.org/cookies')
print(response.text)
#输出
#"cookies": {
#    "number": "123456789"
#  }


#证书验证
#当使用requests.get请求一个https协议的站点，首先会检测证书是否合法
#response=requests.get('https://www.12306.cn')
#print(response.status_code)
#输出：requests.exceptions.SSLError:
# HTTPSConnectionPool(host='www.12306.cn', port=443):
# Max retries exceeded with url:
# / (Caused by SSLError(SSLError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:777)'),))
# 当证书不合法时，会出现错误信息（SSL_ERROR）

#可以设置不进行证书验证（默认开启验证）
response=requests.get('https://www.12306.cn',verify=False)
print(response.status_code)
#输出：200
#同时会有 未验证 警告

#可以手动设置cert参数，指定本地证书

#代理设置
proxies={
    'http':'http://127.0.0.1:9743',
    'https':'https://127.0.0.1:9743'
}

#如果使用有密码的代理:
proxies={'http':'http://user:password@127.0.0.1:9743/'}

#response=requests.get("http://www.taobao.com",proxies=proxies)
#requests中直接将代理 proxies 作为get的参数传递即可完成代理，而不必构造
#ProxyHandler对象，opener对象，使用open()发起请求等

#超时设置
try:
    response=requests.get('http://www.baidu.com',timeout=0.01)
    print(response.status_code)
except Timeout:
    print('TIMEOUT')

#认证设置
#当某些站点请求时需要提供用户名密码认证
#在get申请中提供 auth 参数
#response=requests.get('http://120.37.34.24:9001',auth=('user','123'))
#print(response.status_code)


#异常处理
try:
    response=requests.get('http://www.baidu.com',timeout=0.05)
    print(response.status_code)
except ReadTimeout:
    print('TimeOut')
except ConnectionError:
    print('ConnectionError')
except RequestException:
    print('RequestError')
