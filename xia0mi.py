# _*_ coding:utf-8 _*_
import sqlite3
import os
import urllib2
import re
import HTMLParser
from bs4 import BeautifulSoup

#将系统默认编码设置为utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

urlList = [];
thumbList = [];

html_parser = HTMLParser.HTMLParser()

urlPattern = re.compile(r'href=.+?"')
namePattern = re.compile(r'title=.+?"')
imgPattern = re.compile(r'data-src=.+?"')

for i in range(1,83+1):
	url = "http://zhuti.xiaomi.com/compound?page=" + str(i) + "&sort=New"
	urlList.append(url)
	
soup = BeautifulSoup(urllib2.urlopen("http://zhuti.xiaomi.com/compound?page=3&sort=New").read())

i = 1

for thumb in soup.findAll("div", {"class" : "thumb"}):
	#解析URL链接
	urlMatch = re.findall(urlPattern,str(thumb))
	print urlMatch[0].replace('"','').replace('href=','')
	
	#解析主题名称
	nameMatch = re.findall(namePattern,str(thumb))
	print html_parser.unescape(nameMatch[0].replace('"','').replace('title=',''))
	
	#解析缩略图链接
	imgMatch = re.findall(imgPattern,str(thumb))
	print imgMatch[0].replace('"','').replace('data-src=','')
	print i
	i = i + 1
	
	print ""
	
	thumbList.append(thumb)


