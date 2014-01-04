# _*_ coding:utf-8 _*_
import sqlite3
import os
import urllib2

#将系统默认编码设置为utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from PIL import Image
from PIL.ExifTags import TAGS
 
def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret

ret = get_exif("/home/xiaochun/123/wallpaper/default_wallpaper.jpg")
print ret

ret = get_exif("/home/xiaochun/hello1.jpg")
print ret
