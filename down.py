# _*_ coding:utf-8 _*_
import sqlite3
import os
import urllib2

#将系统默认编码设置为utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#连接数据库
con = sqlite3.connect("mimi.db")
cur = con.cursor()

for i in range(1,2+1):
	
	#从数据库中检索出更新时间和Pageurl
	sql = "select 更新时间,PageUrl from content where id = " + str(i)
	cur.execute(sql)
	res = cur.fetchone()
	updateTime = res[0]
	pageUrl = res[1]
	
	#根据PageUrl构建主题文件的ID和下载链接
	themeID = pageUrl.split('/')[-1]
	downUrl = pageUrl.replace("detail","download")
	
	#构建本地存放路径
	localDir = "/home/xiaochun/MIUI/Download/" + themeID
	
	#判断本地路径是否存在，如果不存在则建立该路径
	if not os.path.exists(localDir):
		op = "mkdir " + localDir
		os.system(op)
	
	#构建本地文件名，以更新时间为文件名
	localName = updateTime + ".mtz"
	
	#判断本地文件是否存在，如果不存在则下载该文件
	if not os.path.isfile(localDir + localName):
		op = "wget -O " + localDir + "/" + localName + " " + downUrl
		os.system(op)
	
	i = i + 1
