# _*_ coding:utf-8 _*_
import sqlite3
import os
import urllib2

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

con = sqlite3.connect("url.db")
cur = con.cursor()

for i in range(351,1500+1):
	sql = "select PageUrl from content where id = " + str(i)
	cur.execute(sql)
	res = cur.fetchone()
	pageUrl = res[0]
	downUrl = pageUrl.replace("detail","download")
	
	r = urllib2.urlopen(downUrl.rstrip())
	file_name = urllib2.unquote(r.geturl()).decode('utf8').split('/')[-1]
	op = "wget -O ~/MIUI/Themes/" + str(i) + "." + file_name + " " + downUrl
	os.system(op)
	os.system("sleep 3")
	i = i + 1
