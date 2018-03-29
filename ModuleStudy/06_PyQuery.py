# -*- coding:utf-8 -*-

from pyquery import PyQuery as pq
# PyQuery
# 强大灵活的网页解析库，与jQuery语法类似
# pip3 install pyquery

# 初始化
html='''
<div class="warp">
<div id="container">
    <ul class="list">
        <li class="item-0">first item</li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
        <li class="item1 active"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
</div>
</div>
'''
# 字符串初始化
doc=pq(html)
print(doc('li'))
# PyQuery所使用的是CSS选择器，.选择class, #选择id 标签直接传入

# URL初始化
doc=pq(url='http://www.baidu.com')
print(doc('head'))

# 文件初始化
doc=pq(filename='pyquery_test.html')
print(doc('li'))

# 基本CSS选择器
doc=pq(html)
print(doc('#container .list li'))

# 查找元素
# 子元素
doc=pq(html)
items=doc('.list')
print(type(items))
# <class 'pyquery.pyquery.PyQuery'>
print(items)
lis=items.find('li')
print(type(lis))
# <class 'pyquery.pyquery.PyQuery'>
print(lis)
# 每一次选择都是PyQuery对象，因此可以通过层层嵌套选择

# 查找所有的直接子元素
lis=items.children()
print(type(lis))
# <class 'pyquery.pyquery.PyQuery'>
print(lis)

lis=items.children('.active')
print(lis)

# 父元素
doc=pq(html)
items=doc('.list')
contanier=items.parent()
print(type(contanier))
# <class 'pyquery.pyquery.PyQuery'>
print(contanier)
# 返回父标签里的所有内容

# 所有的父级及以上的标签
contaniers=items.parents()
print(type(contaniers))
# <class 'pyquery.pyquery.PyQuery'>
print(contaniers)
# 再进行一次筛选
parent=contaniers('.warp')
print(parent)

# 兄弟元素
doc=pq(html)
li=doc('.list .item-0.active')
# 在使用选择器连续选择时，条件之间空格表示条件之间的层级关系 没有空格则表示条件之间的并列关系
# 上述选择器选择class为list的子标签下同时满足class为item-0和active的标签
print(li.siblings())
# 继续筛选
print(li.siblings('.item1'))

#  遍历 .items()方法 将多个匹配结果转化为可枚举类型
doc=pq(html)
lis=doc('li').items()
print(type(lis))
# <class 'generator'>
for li in lis:
    print(type(li))
    # 单个元素类型还是<class 'pyquery.pyquery.PyQuery'>
    print(li)

# 获取信息
# 获取属性
doc=pq(html)
a=doc('.item-0.active a')
print(a)
# <a href="link3.html"><span class="bold">third item</span></a>
print(a.attr('href'))
# link3.html
print(a.attr.href)
# link3.html

# 获取文本(被标签包含的文本内容) .text()
a=doc('.item-0.active a')
print(a)
# <a href="link3.html"><span class="bold">third item</span></a>
print(a.text())
# third item

# 获取HTML .html()
li=doc('.item-0.active')
print(li)
# <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
print(li.html())
# <a href="link3.html"><span class="bold">third item</span></a>

# DOM操作
# add_Class() remove_Class()
doc=pq(html)
li=doc('.item-0.active')
print(li)
# <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
li.remove_class('active')
print(li)
# <li class="item-0"><a href="link3.html"><span class="bold">third item</span></a></li>
li.add_class('active')
print(li)
# <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>

# attr,css 修改或增加属性，修改或增加 style
doc=pq(html)
li=doc('.item-0.active')
print(li)
# <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
li.attr('name','link')
print(li)
# <li class="item-0 active" name="link"><a href="link3.html"><span class="bold">third item</span></a></li>
li.css('font-size','14px')
print(li)
# <li class="item-0 active" name="link" style="font-size: 14px"><a href="link3.html"><span class="bold">third item</span></a></li>

# remove() 删除指定的标签
html='''
    <div class="warp">
        Hello,world
        <p>This is a paragraph.</p>
        </div>
'''
doc=pq(html)
div=doc('.warp')
print(div.text())
# Hello,world
# This is a paragraph.
div.remove('p')
print(div)
# <div class="warp">
#        Hello,world
#        </div>
print(div.text())
# Hello,world

# 伪类选择器
html='''
<div class="warp">
<div id="container">
    <ul class="list">
        <li class="item-0">first item</li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
        <li class="item1 active"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
</div>
</div>
'''
doc=pq(html)
li=doc('li:first-child')
# 选取li标签中的 第一个
print(li)
# <li class="item-0">first item</li>

li=doc('li:last-child')
# 选取li标签中的 最后一个
print(li)
# <li class="item-0"><a href="link5.html">fifth item</a></li>

li=doc('li:nth-child(2)')
# 选取li标签中的 第二个
print(li)
# <li class="item-1"><a href="link2.html">second item</a></li>

li=doc('li:gt(2)')
# 选取li标签中的 序号比2大的
print(li)
# <li class="item1 active"><a href="link4.html">fourth item</a></li>
# <li class="item-0"><a href="link5.html">fifth item</a></li>

li=doc('li:nth-child(2n)')
# 选取li标签中的 序号为偶数的
print(li)
# <li class="item-1"><a href="link2.html">second item</a></li>
# <li class="item1 active"><a href="link4.html">fourth item</a></li>

li=doc('li:contains(second)')
# 选取li标签中的 文本中包含"second"的
print(li)
# <li class="item-1"><a href="link2.html">second item</a></li>
