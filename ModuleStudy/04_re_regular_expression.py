# -*- coding:utf-8 -*-
#re库 & 正则表达式
import re
import requests

#http://tool.oschina.net/regex  开源中国正则表达式在线测试工具（常用正则表达式）

#re.match
#re.match 尝试从字符串的起始位置(第一个字符)匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none
#re.match(pattern,string,flags=0)


content='Hello 123 4567 World_This is a Regex Demo'

#最常规匹配
print(len(content))
result=re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$',content)
print(result)
print(result.group())
print(result.span())
#输出
#41
#<_sre.SRE_Match object; span=(0, 41), match='Hello 123 4567 World_This is a Regex Demo'>
#Hello 123 4567 World_This is a Regex Demo
#(0, 41)  span()匹配到的字符串长度

#泛匹配
result=re.match('^Hello.*Demo$',content)
print(result.group())
#输出
#Hello 123 4567 World_This is a Regex Demo

#目标匹配
#使用()确定选取目标,通过group()中传入参数确定选取部分
content='Hello 1234567 World_This is a Regex Demo'
result=re.match('^Hello\s(\d+)\s.*Demo$',content)
print(result.group(1))
print(result.span())
#输出
#1234567
#(0, 40)

#贪婪匹配   .*
content='Hello 1234567 World_This is a Regex Demo'
result=re.match('^H.*(\d+).*Demo$',content)
print(result)
print(result.group(1))
#输出
#<_sre.SRE_Match object; span=(0, 40), match='Hello 1234567 World_This is a Regex Demo'>
#7
#输出结果并不是 1234567 是由于.*会尽可能保证覆盖尽可能多的字符内容，而\d+ 表示至少一个数字
#因此前面的123456被.*所覆盖

#非贪婪匹配  .*?
result=re.match('^H.*?(\d+).*Demo$',content)
print(result)
print(result.group(1))
#输出
#<_sre.SRE_Match object; span=(0, 40), match='Hello 1234567 World_This is a Regex Demo'>
#1234567

#匹配模式
content='Hello 1234567 World_This \nis a Regex Demo'
result=re.match('^He.*?(\d+).*?Demo$',content)
print(result)
#输出结果
#None   content中包含换行符，而 . 是不能匹配换行符，因此无法匹配出正确结果

#使用 re.S 更换匹配模式，. 就可以匹配任一字符，包括换行符
content='Hello 1234567 World_This \nis a Regex Demo'
result=re.match('^He.*?(\d+).*?Demo$',content,re.S)
print(result)
print(result.group(1))
#输出
#<_sre.SRE_Match object; span=(0, 41), match='Hello 1234567 World_This \nis a Regex Demo'>
#1234567

#转义
content='price is $5.00'
result=re.match('price is $5.00',content)
print(result)
#输出
#None
#原因在于 $ . 在正则表达式中有特殊含义 如果要表示原本的字符意义，需要使用转义
result=re.match('price is \$5\.00',content)
print(result)
#输出
#<_sre.SRE_Match object; span=(0, 14), match='price is $5.00'>

#re.match()是从给定的字符串的第一个字符开始匹配，如果第一个字符不符合正则表达式，
#则无法得到正确目标

#re.search
#re.search（）是从给定字符串扫描，然后返回第一个成功的匹配，
#也就是正则表达式不用从字符串的一开始就书写规则，可以只写筛选目标的局部规则
content='Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
result=re.match('Hello.*?(\d+).*?Demo',content)
print(result)
#输出 None
result=re.search('Hello.*?(\d+).*?Demo',content)
print(result)
print(result.group(1))
#输出
# <_sre.SRE_Match object; span=(13, 53), match='Hello 1234567 World_This is a Regex Demo'>
# 1234567

#匹配练习
html='''<div id="songs-list">
	<h2 class="title">经典老歌</h2>
	<p class="introduction">
	</p>
	<ul id="list" class="list-group">
		<li data-view="2">一路上有你</li>
		<li data-view="7">
			<a herf="/2.mp3" singer="任贤齐">沧海一声笑</a>
		</li>
		<li data-view="4" class="active">
			<a herf="/3.mp3" singer="齐秦">往事随风</a>
		</li>
			<li data-view="6"><a herf="/4.mp3" singer="beyond">光辉岁月</a></li>
			<li data-view="5"><a herf="/5.mp3" singer="陈慧琳">记事本</a></li>
		</li>
		<li data-view="5">
			<a herf="/6.mp3" singer="邓丽君">但愿人长久</a>
		</li>
	</ul>
</div>'''
result=re.search('<a.*?singer="(.*?)">(.*?)</a>',html,re.S)
print(result)
#<_sre.SRE_Match object; span=(173, 212), match='<a herf="/2.mp3" singer="任贤齐">沧海一声笑</a>'>
#re.search()只返回第一个符合要求的结果

#re.findall 查询所有符合条件的所有结果
result=re.findall('<a.*?herf="(.*?)".*?singer="(.*?)">(.*?)</a>',html,re.S)
print(result)
#输出
#[('/2.mp3', '任贤齐', '沧海一声笑'), ('/3.mp3', '齐秦', '往事随风'), ('/4.mp3', 'beyond', '光辉岁月'), ('/5.mp3', '陈慧琳', '记事本'), ('/6.mp3', '邓丽君', '但愿人长久')]
#返回列表，每个元素为一个元组
for items in result:
    print(items[0],items[1],items[2])
#输出
#/2.mp3 任贤齐 沧海一声笑
#/3.mp3 齐秦 往事随风
#/4.mp3 beyond 光辉岁月
#/5.mp3 陈慧琳 记事本
#/6.mp3 邓丽君 但愿人长久

#输出所有的歌名
result=re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*</li>',html,re.S)
print(result)
#输出
for items in result:
    print(items[1])
#输出
#一路上有你
#沧海一声笑
#往事随风
#光辉岁月
#记事本
#但愿人长久

#re.sub 字符串替换   re.sub(re表达式,要替换成的字符串，查询字符串 )
content='Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
result=re.sub('\d+',"MajorTom",content)
print(result)
#输出
#Extra stings Hello MajorTom World_This is a Regex Demo Extra stings

html='''<div id="songs-list">
	<h2 class="title">经典老歌</h2>
	<p class="introduction">
	</p>
	<ul id="list" class="list-group">
		<li data-view="2">一路上有你</li>
		<li data-view="7">
			<a herf="/2.mp3" singer="任贤齐">沧海一声笑</a>
		</li>
		<li data-view="4" class="active">
			<a herf="/3.mp3" singer="齐秦">往事随风</a>
		</li>
			<li data-view="6"><a herf="/4.mp3" singer="beyond">光辉岁月</a></li>
			<li data-view="5"><a herf="/5.mp3" singer="陈慧琳">记事本</a></li>
		</li>
		<li data-view="5">
			<a herf="/6.mp3" singer="邓丽君">但愿人长久</a>
		</li>
	</ul>
</div>'''
#将<a.*?></a>标签删除
result=re.sub('<a.*?>|</a>',"",html)
print(result)
#再提取歌名信息
results=re.findall('<li.*?\s*?(\w+)\s*?</li>',result,re.S)
for item in results:
    print(item)
#输出
#一路上有你
#沧海一声笑
#往事随风
#光辉岁月
#记事本
#但愿人长久

#re.compile
#将正则字符串编译成为正则表达式对象,以便复用这个对象
content='''Hello 1234567 World_This 
        is a Regex Demo'''
pattern=re.compile('Hello.*?Demo',re.S)
result=re.findall(pattern,content)
print(result)
#输出
#['Hello 1234567 World_This \n        is a Regex Demo']


#使用正则表达式提取 豆瓣图书 信息
response=requests.get('https://book.douban.com/')
contents=response.text
print(contents)

content='''<ul class="list-col list-col5 list-express slide-item">
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/27614904/?icn=index-editionrecommend" title="房思琪的初恋乐园">
                <img src="https://img3.doubanio.com/lpic/s29651121.jpg" class=""
                  width="115px" height="172px" alt="房思琪的初恋乐园">
              </a>
            </div>
                <div class="intervenor-info">
                    <img src="https://img3.doubanio.com/f/book/ef040178fab1770d60e3f2f12ba4c7aa70714396/pics/book/partner/jd_recommend.png" class='jd-icon' width="16" height="16"/> 
                    <span>推荐</span>
                </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/27614904/?icn=index-editionrecommend"
                  title="房思琪的初恋乐园">房思琪的初恋乐园</a>
              </div>
              <div class="author">
                林奕含
              </div>
              <div class="more-meta">
                <h4 class="title">
                  房思琪的初恋乐园
                </h4>
                <p>
                  <span class="author">
                    林奕含
                  </span>
                  /
                  <span class="year">
                    2018-1
                  </span>
                  /
                  <span class="publisher">
                    北京联合出版公司
                  </span>
                </p>
                <p class="abstract">
                  
                  令人心碎却无能为力的真实故事。
向死而生的文学绝唱  打动万千读者的年度华语小说。
李银河 戴锦华 骆以军 张悦然 冯唐 詹宏志 蒋方舟 史航 等多位学者作家社会名人郑重推荐。
痛苦的际遇是如此难以分享，好险这个世界还有文学。
我下楼拿作文给李老师改。他掏出来，我被逼到涂在墙上。老师说了九个字：“不行的话，嘴巴可以吧。”我说了五个字：“不行，我不会。”他就塞进...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/27592929/?icn=index-editionrecommend" title="克苏鲁神话Ⅱ">
                <img src="https://img3.doubanio.com/lpic/s29625884.jpg" class=""
                  width="115px" height="172px" alt="克苏鲁神话Ⅱ">
              </a>
            </div>
                <div class="intervenor-info">
                    <img src="https://img3.doubanio.com/f/book/ef040178fab1770d60e3f2f12ba4c7aa70714396/pics/book/partner/jd_recommend.png" class='jd-icon' width="16" height="16"/> 
                    <span>推荐</span>
                </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/27592929/?icn=index-editionrecommend"
                  title="克苏鲁神话Ⅱ">克苏鲁神话Ⅱ</a>
              </div>
              <div class="author">
                [美] H.P.洛夫克拉夫特
              </div>
              <div class="more-meta">
                <h4 class="title">
                  克苏鲁神话Ⅱ
                </h4>
                <p>
                  <span class="author">
                    [美] H.P.洛夫克拉夫特
                  </span>
                  /
                  <span class="year">
                    2018-1-1
                  </span>
                  /
                  <span class="publisher">
                    浙江文艺出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  《克苏鲁神话》被誉为20世纪最伟大、最具影响力的恐怖小说体系，作者是H.P·洛夫克拉夫特——或者“爱手艺”。
假设你的脚边有一只蚂蚁在爬，你不会在意有没有踩死它，因为它太渺小了，是死还是活，对你来说没有分毫影响。在“克苏鲁神话”中描述的远古邪神的眼中，人类就是那只蚂蚁。
洛夫克拉夫特所倡导的“宇宙主义”，即人类远非世界的主宰者，在尚未探索的未知宇...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/27622215/?icn=index-editionrecommend" title="在耶鲁精进">
                <img src="https://img3.doubanio.com/lpic/s29700193.jpg" class=""
                  width="115px" height="172px" alt="在耶鲁精进">
              </a>
            </div>
                <div class="intervenor-info">
                    <img src="https://img3.doubanio.com/f/book/ef040178fab1770d60e3f2f12ba4c7aa70714396/pics/book/partner/jd_recommend.png" class='jd-icon' width="16" height="16"/> 
                    <span>推荐</span>
                </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/27622215/?icn=index-editionrecommend"
                  title="在耶鲁精进">在耶鲁精进</a>
              </div>
              <div class="author">
                王烁
              </div>
              <div class="more-meta">
                <h4 class="title">
                  在耶鲁精进
                </h4>
                <p>
                  <span class="author">
                    王烁
                  </span>
                  /
                  <span class="year">
                    2018-1
                  </span>
                  /
                  <span class="publisher">
                    民主与建设出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  财新传媒主编王烁，被遴选为2016年度耶鲁世界学人，并从2016年9月开始在美国游学。他将游学期间的见闻和学习笔记整理汇总，集结成为本书内容。
全书分为耶鲁故事、极简金融课、极简谈判课、财智逻辑、在美国看美国、大学•问•答网友六个部分，讲述了作者在耶鲁大学的学习与生活中收获的识见与体悟，引领读者近距离接触前沿的知识思维。
从耶鲁大学精品课程的学习笔...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30129112/?icn=index-editionrecommend" title="笛卡尔的错误">
                <img src="https://img1.doubanio.com/lpic/s29677029.jpg" class=""
                  width="115px" height="172px" alt="笛卡尔的错误">
              </a>
            </div>
                <div class="intervenor-info">
                    <img src="https://img3.doubanio.com/f/book/ef040178fab1770d60e3f2f12ba4c7aa70714396/pics/book/partner/jd_recommend.png" class='jd-icon' width="16" height="16"/> 
                    <span>推荐</span>
                </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30129112/?icn=index-editionrecommend"
                  title="笛卡尔的错误">笛卡尔的错误</a>
              </div>
              <div class="author">
                [美] 安东尼奥·达马西奥
              </div>
              <div class="more-meta">
                <h4 class="title">
                  笛卡尔的错误
                </h4>
                <p>
                  <span class="author">
                    [美] 安东尼奥·达马西奥
                  </span>
                  /
                  <span class="year">
                    2018-2
                  </span>
                  /
                  <span class="publisher">
                    湛庐文化/北京联合出版公司
                  </span>
                </p>
                <p class="abstract">'''
pattern=re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)">.*?src="(.*?)"\sclass.*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>',re.S)
result=re.findall(pattern,content)
for item in result:
    link,title,img,author,time=item
    re.sub('\s*',"",author)
    re.sub('\s*',"",time)
    print("Link:"+link)
    print("title:"+title)
    print("img:"+img)
    print("author:"+author)
    print("time:"+time)
