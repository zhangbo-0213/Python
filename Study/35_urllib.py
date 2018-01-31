import urllib2
web=urllib2.urlopen('http://www.baidu.com')
content=web.read()
print content
