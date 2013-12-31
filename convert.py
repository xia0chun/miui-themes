# -*- coding: utf-8 -*-  
import HTMLParser
import sqlite3

#将系统默认编码设置为utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#连接数据库
con = sqlite3.connect("/home/xiaochun/Project/source/mimi.db")
cur = con.cursor()

for i in range(2300,2362+1):
	#先根据id检索出主题名称和PageUrl
	sql = "select 名称,PageUrl from content where id = " + str(i)
	cur.execute(sql)
	res = cur.fetchone()
	themeName = res[0]
	pageUrl = res[1]
	
	#HTML转义字符处理
	html_parser = HTMLParser.HTMLParser()
	trueThemeName = html_parser.unescape(themeName)
	
	#根据PageUrl替换名称
	sql = 'update content set 名称 = "' + trueThemeName + '" where PageUrl = "' + pageUrl + '"'
	cur.execute(sql)
	con.commit()
	
	print str(i) + ". " + trueThemeName
	
	i = i + 1
