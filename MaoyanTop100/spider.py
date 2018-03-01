# -*- coding: utf-8 -*-
import json

import os
import requests
from requests.exceptions import RequestException
from multiprocessing import Pool
from urllib.request import urlretrieve
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
            'name':item[2],
            'actor':item[3].strip()[3:],
            'releasetime':item[4].strip()[5:],
            'index':item[0],
            'image':item[1],
            'score':item[5]+item[6]
        }

#定义写入文件的方法，将结果保存到本地
def write_to_file(contents):
    #使用with as 语法，确保在发生异常时能正常退出
    with open('result.txt','a',encoding='utf-8') as f:
        #使用json解析，将字典元素解析成字符串
        f.write(json.dumps(contents,ensure_ascii=False)+'\n')
        f.close()

#定义保存图片至本地的方法
def save_img(img_url,file_name,file_path="D:\\Downloads\\img\\maoyantop100"):
    #将图片保存到文件夹file_path中，默认为D:\Downloads\img\maoyantop100 文件夹
    try:
        if not os.path.exists(file_path):
            print("文件夹{0}不存在，重新建立".format(file_path))
            #使用os.makedirs()可以建立多级目录
            os.makedirs(file_path)
        #获得图片后缀(os.path.splitext:分离文件名与扩展名)
        file_suffix=os.path.splitext(img_url)[1][:4]
        #拼接图片名（包含路径）
        filename='{}{}{}{}'.format(file_path,os.sep,file_name,file_suffix)
        #下载图片，保存在文件中
        urlretrieve(img_url,filename=filename)
        print('文件：{0}下载完成'.format(filename))
    except IOError as e:
        print('文件操作失败',e)
    except Exception as e:
        print('错误',e)




def main(offset):
    url='http://maoyan.com/board/4?offset='+str(offset)
    html=get_one_page(url)
    for item in prase_one_page(html):
        print(item)
        write_to_file(item)
        save_img(item['image'],item['index']+item['name'])

#__name=='__main__' 表示如果直接运行该模块，以下函数将会被执行
#如果该模块被其他模块引用，则以下代码不执行
if __name__=='__main__':
    #使用多进程处理，创建进程池
    pool=Pool()
    pool.map(main,[i*10 for i in range(10)])
    pool.close()

