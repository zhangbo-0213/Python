# -*- coding:utf-8 -*-
# BeautifulSoup 灵活高效的网页解析库，支持多种解析器
# 利用它不用编写正则表达式即可方便地实现网页信息的提取
# 安装 pip3 install beautifulsoup4

from bs4 import BeautifulSoup

html='''<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and 
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''

# 用法实例
# 构建BeautifulSoup对象，传入指定的html文本和解析器（这里选择lxml解析器）
soup=BeautifulSoup(html,'lxml')
# soup.prettify() 方法将传入的beautifulsoup对象的html文本自动补全(标签对自动补全)，形成标准的html文本
print(soup.prettify())
# 提取soup对象的html文本中title标签内的内容
print(soup.title.string)

# 标签选择器

# 选择元素（结果包含标签本身）
print(soup.title)
print(type(soup.title))
print(soup.head)
print(soup.p) #标签只返回第一个标签匹配结果

# 获取名称
print(soup.title.name)
# 返回最外层标签名

# 获取属性（两种获取标签内对应属性名的值）
print(soup.p.attrs['name'])
print(soup.p['name'])

# 获取标签内容
print(soup.p.string)

# 嵌套选择(标签内包含标签进一步选择)
print(soup.head.title.string)

# 子节点和子孙节点（标签之间包含层级关系，如何选择子结点）
html='''<html><head><title>The Dormouse's story</title></head>
<body>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and 
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''
soup=BeautifulSoup(html,'lxml')
print(soup.p.contents)
# 返回结果为一个列表，列表元素为每一个闭合的子标签及其内容

# 返回子节点的另一种方法
print(soup.p.children)  #soup.p.children是list_iterator object迭代器类型
for i,child in enumerate(soup.p.children):
    print(i,child)

# 返回子孙结点
print(soup.p.descendants)
for i,child in enumerate(soup.p.descendants):
    print(i,child)

# 返回父节点
print(soup.a.parent)

# 返回祖先节点
print(list(enumerate(soup.a.parents)))

# 返回兄弟结点
print(list(enumerate(soup.a.next_siblings)))
print(list(enumerate(soup.a.previous_siblings)))


# 标准选择器
# find_all(name,attrs,recursive,text,**kwargs)
html='''<div class="pannel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="element" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
# find_all
soup=BeautifulSoup(html,'lxml')
print(soup.find_all('ul'))
print(type(soup.find_all('ul')[0]))
# 输出：<class 'bs4.element.Tag'>

# 使用find_all嵌套查找目标标签的子标签
soup=BeautifulSoup(html,'lxml')
ul=soup.find_all('ul')
for li in ul:
    print(li.find_all('li'))

# attrs参数(标签内属性)
soup=BeautifulSoup(html,'lxml')
print(soup.find_all(attrs={'id':'list-1'}))
print(soup.find_all(id='list-1'))
print(soup.find_all(attrs={'name':'elements'}))


#根据text(文本内容选择)
soup=BeautifulSoup(html,'lxml')
print(soup.find_all(text='Foo'))
# 输出:['Foo', 'Foo']
# 输出结果只包含文本，并不包括所在的标签

# find方法：返回单个元素，find_all方法：返回所有元素
# find(name,attrs,recurive,text,**kwargs)
# find与find_all用法一致，只是返回结果不同
soup=BeautifulSoup(html,'lxml')
print(soup.find('ul'))
print(type(soup.find('ul')))
print(soup.find('page'))

#find_parent() find_parents()
#返回父节点，返回祖先节点

#find_next_sibling() find_next_siblings()
#返回下一个兄弟节点，返回后面的所有兄弟节点

#find_previous_sibling() find_previous_siblings()
#返回前一个兄弟节点，返回前面所有兄弟节点

#find_all_next find_next()
#返回节点后所有符合条件的节点，返回第一个符合条件的节点

#find_all_previous() find_previous()
#返回节点前所有符合条件的节点 返回前面第一个符合条件的节点

#CSS选择器
#通过select()直接传入CSS选择器即可完成选择
html='''<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="element" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
#使用select()方法选择在传入参数时，
# 若选择class 需要在class名前加.
# 若选择id 需要在id名前加#
# 直接选择标签时，不需要加符号
# 连续选择时，各个选择参数之间使用 空格
soup=BeautifulSoup(html,'lxml')
print(soup.select('.panel .panel-heading'))
print(soup.select('ul li'))
print(soup.select('#list-2 .element'))
print(type(soup.select('ul')[0]))

#CSS选择器嵌套选择
soup=BeautifulSoup(html,'lxml')
for ul in soup.select('ul'):
    print(ul.select('li'))

#获取属性(使用[])
soup=BeautifulSoup(html,'lxml')
for ul in soup.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])
#输出：
#list-1
#list-1
#list-2
#list-2

#获取内容(get_text)
soup=BeautifulSoup(html,'lxml')
for li in soup.select('li'):
    print(li.get_text())

#推荐使用lxml解析库,必要时使用html.parser
#标签选择器筛选功能弱但是速度快
#建议使用find() find_all()查询匹配单个结果或多个结果
#如果对CSS选择器熟悉可以使用select()
#熟悉对应获取文本属性的文本值的方法
