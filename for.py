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

urlPattern = re.compile(r'href=.+?"')
namePattern = re.compile(r'title=.+?"')
imgPattern = re.compile(r'data-src=.+?"')
html_parser = HTMLParser.HTMLParser()

for i in range(1,84+1):
	
	j = 1
	url = "http://zhuti.xiaomi.com/compound?page=" + str(i) + "&sort=New"
	soup = BeautifulSoup(urllib2.urlopen(url).read())
	
	
	for thumb in soup.findAll("div",{"class" : "thumb"}):
		urlMatch = re.findall(urlPattern,str(thumb))
		print urlMatch[0].replace('"','').replace('href=','')
		
		nameMatch = re.findall(namePattern,str(thumb))
		print html_parser.unescape(nameMatch[0].replace('"','').replace('title=',''))
		
		imgMatch = re.findall(imgPattern,str(thumb))
		print imgMatch[0].replace('"','').replace('data-src=','')
		
		print str((i - 1) * 30 + j)
		print ""
		j = j + 1
	
	time.sleep(2)
