#encoding:utf-8

# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

import selenium
from selenium import webdriver
import os

#os.path.basename("C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")
#启动火狐浏览器
#browser = webdriver.Firefox()

#启动Chrome浏览器
browser = webdriver.Firefox()

#打开一个网页
browser.get("http://www.baidu.com")
print browser.title

if '百度' in browser.title:
    print("yes")
else:
    print("no")

