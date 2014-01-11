# _*_ coding:utf-8 _*_
import sqlite3
import os
import urllib2
import re
import HTMLParser
import time
from bs4 import BeautifulSoup

#将系统默认编码设置为utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#各项属性的正则匹配参数
themeUrlPattern = re.compile(r'href=.+?"')
themeNamePattern = re.compile(r'title=.+?"')
thumbUrlPattern = re.compile(r'data-src=.+?"')

#html解析
html_parser = HTMLParser.HTMLParser()

for i in range(1,84+1):
	
	j = 1
	url = "http://zhuti.xiaomi.com/compound?page=" + str(i) + "&sort=New"
	soup = BeautifulSoup(urllib2.urlopen(url).read())
	
	
	for thumb in soup.findAll("div",{"class" : "thumb"}):
		#解析themeUrl
		themeUrl = re.findall(themeUrlPattern,str(thumb))
		print themeUrl[0].replace('"','').replace('href=','')
		
		#解析themeName
		themeName = re.findall(themeNamePattern,str(thumb))
		print html_parser.unescape(themeName[0].replace('"','').replace('title=',''))
		
		#解析thumbUrl
		thumbUrl = re.findall(thumbUrlPattern,str(thumb))
		print thumbUrl[0].replace('"','').replace('data-src=','')
		
		print str((i - 1) * 30 + j)
		print ""
		j = j + 1
	
	time.sleep(2)
