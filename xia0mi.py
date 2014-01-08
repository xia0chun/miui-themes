# _*_ coding:utf-8 _*_
import sqlite3
import os
import urllib2
from bs4 import BeautifulSoup

#将系统默认编码设置为utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

urllist = [];

for i in range(1,83+1):
	url = "http://zhuti.xiaomi.com/compound?page=" + str(i) + "&sort=New"
	urllist.append(url)
	
soup = BeautifulSoup(urllib2.urlopen("http://zhuti.xiaomi.com/compound?page=1&sort=New").read())

for thumb in soup.findAll("div", {"class" : "thumb"}):
	print thumb
