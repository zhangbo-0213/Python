# -*- coding:utf-8 -*-
# selenium 自动化测试工具，支持多种浏览器
# 爬虫中主要用来解决JavaScript渲染的问题，在使用Urllib或Requests获取请求无法解析
# 目标站点可能是使用JavaScript进行渲染，可以使用Selenium库进行解析

# pip3 install selenium
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# 基本用法

# 声明一个浏览器驱动对象

browser=webdriver.Chrome()
try:
    browser.get('http://www.baidu.com')
    input=browser.find_element_by_id('kw')
    # 输入关键字
    input.send_keys('Python')
    # 输入回车
    input.send_keys(Keys.ENTER)
    # 设置等待
    wait=WebDriverWait(browser,10)
    # 等待元素ID 为 ‘content_left’ 的元素被加载出来
    wait.until(EC.presence_of_element_located((By.ID,'content_left')))

    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
finally:
    browser.close()


# 声明浏览器对象
browser=webdriver.Chrome()
# browser=webdriver.Firefox()
# browser=webdriver.Edge()
# browser=webdriver.PhantomJS()
# browser=webdriver.Safari()
browser.close()

# 访问页面
browser=webdriver.Chrome()
browser.get('https://www.taobao.com')
print(browser.page_source)
browser.close()

# 查找元素

# 通过选择器查找单个元素（如：找到对应的输入框输入内容或者找到按钮进行点击）
browser=webdriver.Chrome()
browser.get('https://www.taobao.com')
input_1=browser.find_element_by_id('q')
input_2=browser.find_element_by_css_selector('#q')
input_3=browser.find_element_by_xpath('//*[@id="q"]')
input_4=browser.find_element(By.ID,'q')
print(input_1,input_2,input_3,input_4)
browser.close()
# 常用查找元素方法
# browser.find_element_by_name()
# browser.find_element_by_xpath()
# browser.find_element_by_link_text()
# browser.find_element_by_partial_link_text()
# browser.find_element_by_tag_name()
# browser.find_element_by_class_name()
# browser.find_element_by_css_selector()

# 查找多个元素
browser=webdriver.Chrome()
browser.get('https://www.taobao.com')
lis=browser.find_elements(By.CSS_SELECTOR,'.service-bd li')
print(lis)
browser.close()
# 常用查找多个元素方法
# browser.find_elements_by_name()
# browser.find_elements_by_xpath()
# browser.find_elements_by_link_text()
# browser.find_elements_by_partial_link_text()
# browser.find_elements_by_tag_name()
# browser.find_elements_by_class_name()
# browser.find_elements_by_css_selector()

# 元素交互操作
# 对获取的元素调用交互方法（获取到文本框或按钮）
browser=webdriver.Chrome()
browser.get('https://www.taobao.com')
# 找到输入框的元素 id 并选择该元素
input=browser.find_element_by_id('q')
# 对文本框元素输入 搜索内容
input.send_keys('iPhone')
time.sleep(1)
input.clear()
input.send_keys('iPad')
button=browser.find_element_by_class_name('btn-search')
button.click()


# 交互动作
# 将动作附加到动作链中串行执行（并非单一点击动作，而是连续动作，例如拖拽，需要引入 ActionChains）
browser=webdriver.Chrome()
url='http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
source=browser.find_element_by_id('draggable')
target=browser.find_element_by_id('droppable')
actions=ActionChains(browser)
actions.drag_and_drop(source,target)
actions.perform()
# 更多操作参考：http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.action_chains

# 执行JavaScript  browser.execute_script()
# 传入JS命令执行动作
# 例如打开知乎网页，下拉到最下端，然后进行提示
browser=webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
browser.execute_script('alert("To Bottom")')

# 获取元素信息
# 获取属性
browser=webdriver.Chrome()
browser.get('http://www.zhihu.com/explore')
logo=browser.find_element_by_id('zh-top-link-logo')
print(logo)
print(logo.get_attribute('class'))

# 获取文本值
browser=webdriver.Chrome()
browser.get('http://www.zhihu.com/explore')
input=browser.find_element_by_class_name('zu-top-add-question')
print(input.text)

# 获取ID、位置、标签、大小
browser=webdriver.Chrome()
browser.get('http://www.zhihu.com/explore')
input=browser.find_element_by_class_name('zu-top-add-question')
print(input.id)
print(input.location)
print(input.tag_name)
print(input.size)

# Frame 网页中独立的窗口，需要从父窗口切换到子窗口再进行元素选择和操作
browser=webdriver.Chrome()
browser.get('http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
browser.switch_to.frame('iframeResult')
source=browser.find_element_by_id('draggable')
try:
    logo=browser.find_element_by_class_name('logo')
except NoSuchElementException:
    print('No Logo')
browser.switch_to.parent_frame()
logo=browser.find_element_by_class_name('logo')
print(logo)
print(logo.text)

# 等待

# 隐式等待(网络情况不良时可以进行等待后再查找)
# 当使用了隐式等待执行测试地时候，如果WebDriver没有在DOM中找到目标元素，将继续等待，超出设定时间后则抛出找不到元素异常
# 也就是说，当查找元素没有立即出现的时候，隐式等待会等待一段时间后再进行DOM元素的查找，默认时间是0
browser=webdriver.Chrome()
browser.get('http://www.zhihu.com/explore')
browser.implicitly_wait(10)
input=browser.find_element_by_id('zh-top-nav-explore')
print(input.text)

# 显示等待
# 指定一个条件和显式等待时间，如果指定时间内条件不成立会一直等待，直到超时等待时间条件不成立会抛出异常，指定时间内成立返回内容
# 确保交互动作前需要等待的操作能正常进行不中断
browser=webdriver.Chrome()
browser.get('https://www.taobao.com')
wait=WebDriverWait(browser,10)
input=wait.until(EC.presence_of_element_located((By.ID,'q')))
button=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.btn-search')))
browser.execute_script('alert("Alert")')
alert=wait.until(EC.alert_is_present())
print(input,button,alert)

# 常用的判断条件：
# title_is 标题是某内容
# title_contains 标题包含某内容
# presence_of_element_located 元素加载出，传入定位元组，如(By.ID, 'p')
# visibility_of_element_located 元素可见，传入定位元组
# visibility_of 可见，传入元素对象
# presence_of_all_elements_located 所有元素加载出
# text_to_be_present_in_element 某个元素文本包含某文字
# text_to_be_present_in_element_value 某个元素值包含某文字
# frame_to_be_available_and_switch_to_it frame加载并切换
# invisibility_of_element_located 元素不可见
# element_to_be_clickable 元素可点击
# staleness_of 判断一个元素是否仍在DOM，可判断页面是否已经刷新
# element_to_be_selected 元素可选择，传元素对象
# element_located_to_be_selected 元素可选择，传入定位元组
# element_selection_state_to_be 传入元素对象以及状态，相等返回True，否则返回False
# element_located_selection_state_to_be 传入定位元组以及状态，相等返回True，否则返回False
# alert_is_present 是否出现Alert
# 更多操作参考：http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions

# 浏览器前进后退
browser=webdriver.Chrome()
browser.get('https://www.baidu.com/')
browser.get('https://www.taobao.com/')
browser.get('https://www.python.org/')
browser.back()
time.sleep(1)
browser.forward()
browser.close()

# Cookies
browser=webdriver.Chrome()
browser.get('https://www.zhihu.com')
print(browser.get_cookies())
browser.add_cookie({'name':'name','domain':'www.zhihu.com','value':'majortom'})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())

# 浏览器多个选项卡管理
# 使用JS
browser=webdriver.Chrome()
browser.get('http://www.baidu.com')
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to.window(browser.window_handles[1])
browser.get('https://www.taobao.com')
time.sleep(1)
browser.switch_to.window(browser.window_handles[0])
browser.get('https://python.org')

# 异常处理
# 浏览器异常相对较复杂,种类比较多
browser=webdriver.Chrome()
try:
    browser.get('http://www.baidu.com')
except TimeoutException:
    print('Time Out Exception')
try:
    input=browser.find_element_by_id('hello')
except NoSuchElementException:
    print('No Such Element')
# 官网的参考地址：http://selenium-python.readthedocs.io/api.html#module-selenium.common.exceptions
