# -*- coding: utf-8 -*-
import requests
from requests.exceptions import RequestException
import re

# 定义请求单页内容函数
def get_one_page(url):
    try:
        response=requests.get(url)
        # 请求结果根据返回的状态码判断，如果判断码是200，则返回成功
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        return None
    # 添加try except 异常处理

# 定义提取单页内容函数
def prase_one_page(html):
    # re.compile()方法通过一个正则表达式字符串编译生成一个正则表达式对象
    # 字符串中()内的内容为想要的结果，结果本身也需要使用正则表达式表示
    pattern=re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?'
                       '>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">'
                       '(.*?)</i>.*?fraction">(\d+)</i>.*?</dd>',re.S)
    # re.compile(,)第二个参数 re.S 表示 .通配符也包括换行符
    items=re.findall(pattern,html)
    for item in items:
        #使用yield迭代生成器，生成一个可迭代的结果(这里的迭代元素是字典)，每次迭代从上一个迭代结果开始
        yield{
            'index':item[0],
            'image':item[1],
            'name':item[2],
            'actor':item[3].strip()[3:],
            'releasetime':item[4].strip()[5:],
            'score':item[5]+item[6]
        }

def main():
    url='http://maoyan.com/board/4?offset=0'
    html=get_one_page(url)
    for item in prase_one_page(html):
        print(item)

if __name__=='__main__':
    main()
