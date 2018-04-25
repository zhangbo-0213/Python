# -*- coding:utf-8 -*-
# Selenium+Chrome/PhantomJS 爬取淘宝美食
# 模拟输入搜索，得到查询列表，模拟翻页，分析提取商品内容
import re

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as py

from config import *
# 引入Mongo_DB 数据库对象
import pymongo
client=pymongo.MongoClient(MONGO_URL)
db=client[MONGO_DB]

# 使用无界面浏览器 PhantomJS
browser=webdriver.PhantomJS(service_args=SERVICE_ARGS)
browser.set_window_size(1400,900)
wait=WebDriverWait(browser,10)

def search():
    print('开始搜索')
    try:
        browser.get('https://www.taobao.com')
        # 使用显式等待，直到搜索元素被加载完成
        input=wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'#q'))
        )
        # 使用显式等待，直到搜索按钮加载后成为可点击状态
        submit=wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_TSearchForm > div.search-button > button'))
        )
        input.send_keys(KEYWORD)
        submit.click()
        # 等待页数加载完成，获取总页数
        totalpage=wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.total'))
        )
        get_products()
        return totalpage.text
    # 如果出现超时异常，则重新再请求一次
    except TimeoutException:
        return search()

# 定义 翻页动作及翻页后判断 方法
def next_page(page_number):
    print('正在翻页',page_number)
    try:
        # 选择页码输入元素
        input=wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.form > input'))
            )
        # 选择页码跳转确定按钮
        submit=wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit'))
        )
        input.clear()
        input.send_keys(page_number)
        submit.click()
        # 完成翻页后，确定当前页面是否为指定翻页的页码
        wait.until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > ul > li.item.active > span'),str(page_number))
        )
        get_products()
    # 超时异常使用递归再次调用
    except TimeoutException:
        next_page(page_number)

# 定义 单页解析 方法
def get_products():
    # 确保商品列表已经刷新
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-itemlist .items .item')))
    html=browser.page_source
    # 使用 pyQuery 解析库选择对应的元素
    doc=py(html)
    items=doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product={
            'image':item.find('.pic .img').attr('src'),
            'title':item.find('.title').text().replace('\n',''),
            'price':item.find('.price').text().replace('\n',''),
            'deal':item.find('.deal-cnt').text()[:-3],
            'shop':item.find('.shop').text(),
            'location':item.find('.location').text()
        }
        save_to_mongo(product)

def save_to_mongo(result):
    try:
        if db[MONGO_TABLE].insert(result):
            print('保存到MONGODB成功',result)
    except Exception:
        print('保存到MONGODB错误',result)

def main():
    try:
        totalpage=search()
        totalpage=int(re.compile('(\d+)').search(totalpage).group(1))
        for i in range(2,totalpage+1):
            next_page(i)
    except Exception:
        print('爬取出现异常')
    finally:
        browser.close()

if __name__=='__main__':
    main()
