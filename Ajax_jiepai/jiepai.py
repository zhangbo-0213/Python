# -*- coding:utf-8 -*-

import json
import re

import os
from hashlib import md5
from multiprocessing import Pool

import pymongo
import requests
from urllib.parse import urlencode

from bs4 import BeautifulSoup
from requests.exceptions import RequestException

# 导入配置文件
from config import *
# import * 表示config文件中所有的变量都可以引入

# 定义 mongo 对象
client=pymongo.MongoClient(MONGO_URL,connect=False)
db=client[MONGO_DB]


def get_one_index(offset,keyword):
    data={
        'offset':offset,
        'format':'json',
        'keyword':keyword,
        'autoload':'true',
        'count':'20',
        'cur_tab':3
    }
    url='https://www.toutiao.com/search_content/?'+urlencode(data)
    try:
        response=requests.get(url)
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        print('请求索引页错误')
        return None

def prase_page_index(html):
    # 将当前的josn字符串转换成json对象
    data=json.loads(html)
    # 判断返回结果 data 中是否包含 'data' 键值
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')

def get_page_detail(url):
    try:
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
         }
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        print('请求详情页错误')
        return None

def prase_page_detial(html,url):
    soup=BeautifulSoup(html,'lxml')
    title=soup.select('title')[0].get_text()
    images_pattern=re.compile('.parse\((".*?")\),',re.S)
    result=re.search(images_pattern,html)
    if result:
        # print((result.group(1)))
        # result.group(1)指定正则表达式中第一个括号内的提取内容
        # 在python中解开反斜线转义的字符串
        # 使用eval()将字符串中的字典转化为字典类型
        data=json.loads(eval(result.group(1)))
        if data and 'sub_images' in data.keys():
            sub_images=data.get('sub_images')
            images=[item.get('url') for item in sub_images]
            # 图片下载到本地
            title=''.join(re.findall(u'[\u4e00-\u9fff]+',title))
            for image in images:
                download_img(image,title)
            return{
                'title': title,
                'url': url,
                'images': images
            }

def save_to_mongo(result):
    if db[MONGO_TABLE].insert(result):
        print('存储到MongoDB成功',result)
        return True
    return False

def download_img(url,second_path_name):
    print('正在下载',url)
    try:
        response=requests.get(url)
        if response.status_code==200:
            save_img(response.content,second_path_name)
        # response.content 返回页面的二进制结果，一般图片，音频等资源使用二进制内容存储
        # response.text 返回文字内容,获取网页html内容使用text
        return None
    except RequestException:
        print('图片下载发生错误')
        return None

def save_img(content,second_path_name):
    path=IMG_ROOT_PATH+'/'+second_path_name
    if not os.path.exists(path):
        os.makedirs(path)
    file_path="{0}/{1}.{2}".format(path,md5(content).hexdigest(),'jpg')
    if not os.path.exists(file_path):
        with open(file_path,'wb+') as f:
            f.write(content)
            f.close()

def main(offset):
    html=get_one_index(offset,KEYWORD)
    for url in prase_page_index(html):
        html2=get_page_detail(url)
        if html2:
            result=prase_page_detial(html2,url)
            if result:
                # 保存数据到MongoDB
                save_to_mongo(result)


if __name__=='__main__':
    pool = Pool()
    groups=[x*20 for x in range(GROUP_START,GROUP_END+1)]
    pool.map(main,groups)
