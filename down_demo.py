# _*_ coding:utf-8 _*_
import urllib2
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#url = "http://zhuti.xiaomi.com/download/8bc190d9-c286-4a95-b38f-99a2a052e7c4"
url = "http://zhuti.xiaomi.com/download/d3c0e2d7-1af2-4bc0-b6b8-2b6bfbf33250"
r = urllib2.urlopen(url.rstrip())
file_name = urllib2.unquote(r.geturl()).decode('utf8').split('/')[-1]
op = "wget -O " + file_name + " " + url
os.system(op)
