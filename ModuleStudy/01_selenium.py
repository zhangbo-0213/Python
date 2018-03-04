import os
from selenium import webdriver
#chromeDriPath=os.path.abspath(r'E:\Python3\Ptthon3.6Install\Scripts\chromedriver.exe')
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
print(driver.title)
driver.close()
