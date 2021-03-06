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
#lv1
themeUrlPattern = re.compile(r'href=.+?"')
themeNamePattern = re.compile(r'title=.+?"')
thumbUrlPattern = re.compile(r'data-src=.+?"')

#lv2
designerPattern = re.compile(r'设计师.+?\n')
authorPattern = re.compile(r'制作者.+?\n')
sizePattern = re.compile(r'大小.+?\n')
updatePattern = re.compile(r'更新时间.+?\n')
modulesPattern = re.compile(r'包含模块.+?\n')
infoPattern = re.compile(r'class="bd.+?</')
pricePattern = re.compile(r'id="J_buy.+?</')
visibleImgPattern = re.compile(r'<img alt="" src=.+?/>')
invisibleImgPattern = re.compile(r'data-src=.+?/>')

#html解析
html_parser = HTMLParser.HTMLParser()

#根地址
rootUrl = "http://zhuti.xiaomi.com"

for i in range(1,10+1):
	
	j = 1
	url = "http://zhuti.xiaomi.com/compound?page=" + str(i) + "&sort=New"
	soupLv1 = BeautifulSoup(urllib2.urlopen(url).read())
	for detailLv1 in soupLv1.findAll("div",{"class" : "thumb"}):
		#解析themeUrl
		themeUrl = re.findall(themeUrlPattern,str(detailLv1))
		themeUrl = themeUrl[0].replace('"','').replace('href=','')
		print rootUrl + themeUrl
		
		#解析themeName
		themeName = re.findall(themeNamePattern,str(detailLv1))
		themeName = html_parser.unescape(themeName[0].replace('"','').replace('title=',''))
		print themeName
		
		#解析thumbUrl
		thumbUrl = re.findall(thumbUrlPattern,str(detailLv1))
		thumbUrl = thumbUrl[0].replace('"','').replace('data-src=','')
		print thumbUrl
		
		soupLv2 = BeautifulSoup(urllib2.urlopen(rootUrl + themeUrl).read())
		for detailLv2 in soupLv2.findAll("div",{"class" : "mod userinfos"}):
			#解析设计师designer
			designer = re.findall(designerPattern,str(detailLv2))
			print designer[0].replace('\n','').replace('</span>','')
			
			#解析作者author
			author = re.findall(authorPattern,str(detailLv2))
			print author[0].replace('\n','').replace('</span>','')
			
			#解析大小size
			size = re.findall(sizePattern,str(detailLv2))
			print size[0].replace('\n','').replace('</span>','')
			
			#解析更新时间update
			update = re.findall(updatePattern,str(detailLv2))
			print update[0].replace('\n','').replace('</span>','')
			
			#解析包含模块modules
			modules = re.findall(modulesPattern,str(detailLv2))
			print modules[0].replace('\n','').replace('</span>','')
			
		for infoLv2 in soupLv2.findAll("div",{"class" : "mod detail-infos"}):
			#解析资源介绍info
			info = re.findall(infoPattern,str(infoLv2).replace('\n',''))
			print info[0].replace('</','').replace('<div>','').replace('class="bd">','').replace('  ','')
			
		for imgLv2 in soupLv2.findAll("div",{"class" : "thumbnail"}):
			#解析显性图片visibleImg
			visibleImg = re.findall(visibleImgPattern,str(imgLv2).replace('\n',''))
			for img in visibleImg:
				print img.replace('<img alt="" src="','').replace('"/>','') 
			
			#解析隐性图片invisbleImg
			invisibleImg = re.findall(invisibleImgPattern,str(imgLv2).replace('\n',''))
			for img in invisibleImg:
				print img.replace('data-src="','').replace('" src="http://resource.xiaomi.net/miuimarket/lazyload.png"/>','')
			
			
			print str((i - 1) * 30 + j)
			print ""
			j = j + 1
			time.sleep(2)
	
	time.sleep(3)
