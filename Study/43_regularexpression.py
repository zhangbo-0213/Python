# -*- coding: utf-8 -*-
import re
text='Hi,I am Shirley Hilton. I am his wife'
m=re.findall(r'[Hhi]i',text)
# 字符串前的r 表示不对字符串进行转义
print '"[Hhi]i"匹配结果:'
if m:
    print m
else:
    print 'not match'

m=re.findall(r'i.',text)
print '"i."匹配结果:'
if m:
    print m
else:
    print 'not match'

m=re.findall(r'i\S',text)
print '"i\S"匹配结果:'
if m:
    print m
else:
    print 'not match'

m=re.findall(r'I.*e',text)
print '"I.*e"匹配结果:'
if m:
    print m
else:
    print 'not match'

m=re.findall(r'I.*?e',text)
print '"I.*?e"匹配结果:'
if m:
    print m
else:
    print 'not match'



text2='site sea sue sweet see case sse ssee loses'
m=re.findall(r's{2}e',text2)
print text2+'   "s{2}e"匹配结果:'
if m:
    print m
else:
    print 'not match'

print text2+' 中所有以s开头 和 e结尾的单词'
m=re.findall(r'\bs\S*?e\b',text2)
if m:
    print m
else:
    print 'not match'

text3='school__123__和学校'
print text3+' 输出其中的汉字,数字，字母和下划线： '
m=re.findall(r'\w',text3)
if m:
    print m
else:
    print 'not match'

text3='schoolandhome'
print text3+'  使用^进行匹配:'
m=re.findall(r'^sch',text3)
if m:
    print m
else:
    print 'not match'

text3='schoolandhome'
print text3+'  使用$进行匹配:'
m=re.findall(r'e$',text3)
if m:
    print m
else:
    print 'not match'

text3='site sea sue sweet see case sse ssee loses'
print text3+' 中以s开头 和 s结尾的一行'
m=re.findall(r'^s.*s$',text3)
if m:
    print m
else:
    print 'not match'

num='(021)88776543 010-55667890 02584453362 0571 66345673'
n=re.findall('\(?0\d{2,3}[) -]?\d{7,8}',num)
if n:
    print n
else:
    print 'not match'
