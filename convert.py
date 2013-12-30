# -*- coding: utf-8 -*-  
import HTMLParser
import sqlite3

#将系统默认编码设置为utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#连接数据库
con = sqlite3.connect("/home/xiaochun/MIUI/Source/db/mimi.db")
cur = con.cursor()

for i in range(1,10+1):
	sql = "select 名称,PageUrl from content where id = " + str(i)
	cur.execute(sql)
	res = cur.fetchone()
	themeName = res[0]
	pageUrl = res[1]
	
	#HTML转义字符处理
	html_parser = HTMLParser.HTMLParser()
	trueThemeName = html_parser.unescape(themeName)
	
	print trueThemeName
	#print pageUrl
	
	#根据名称重新查询PageUrl
	sql = "select id from content where PageUrl = '" + pageUrl + "'"
	cur.execute(sql)
	res = cur.fetchall()
	print str(len(res))
	
	i = i + 1
