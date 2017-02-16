#encoding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import time

from selenium import webdriver

#启动Chrome浏览器
browser = webdriver.Firefox()

#打开一个网页
browser.get("http://www.maiziedu.com/")
time.sleep(7)
#打印网页的title
print browser.title

#定位登录按钮
tj_login =browser.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/div/a[2]")

account = "maizi_test@139.com";
pwd = 'abc123456'
#点击按钮
tj_login.click()
#定位用户名
id_account = browser.find_element_by_id("id_account_l")
#填写用户名
id_account.send_keys(account)
#定位密码
id_password = browser.find_element_by_id("id_password_l")
#填写密码
id_password.send_keys(pwd)
#点击登录
id_login = browser.find_element_by_id("login_btn")
print "123"
id_login.click()
time.sleep(7)










