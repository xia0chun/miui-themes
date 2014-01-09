# _*_ coding:utf-8 _*_
import sqlite3
import os
import urllib2
import re
from bs4 import BeautifulSoup

#将系统默认编码设置为utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

urlList = [];
thumbList = [];

urlPattern = re.compile(r'href=.+?"')
namePattern = re.compile(r'title=.+?"')
imgPattern = re.compile(r'data-src=.+?"')

for i in range(1,83+1):
	url = "http://zhuti.xiaomi.com/compound?page=" + str(i) + "&sort=New"
	urlList.append(url)
	
soup = BeautifulSoup(urllib2.urlopen("http://zhuti.xiaomi.com/compound?page=1&sort=New").read())

for thumb in soup.findAll("div", {"class" : "thumb"}):
	#解析URL链接
	urlMatch = re.findall(urlPattern,str(thumb))
	print urlMatch[0]
	
	#解析主题名称
	nameMatch = re.findall(namePattern,str(thumb))
	print nameMatch[0].replace('"','').replace('title=','')
	
	#解析缩略图链接
	imgMatch = re.findall(imgPattern,str(thumb))
	print imgMatch[0]
	
	print ""
	
	thumbList.append(thumb)


