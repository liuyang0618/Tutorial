#encoding:utf-8

import time
from selenium import webdriver
#启动火狐浏览器
browser = webdriver.Firefox()
#访问的url
url = 'http://www.maiziedu.com'
#访问url
browser.get(url)
#窗口最大化
browser.maximize_window()
#查找搜索框
login_btn = browser.find_element_by_link_text(u"登录")
#点击登录按钮
login_btn.click()
time.sleep(2)
#点击用户名输入框
account_input = browser.find_element_by_id("id_account_l")
#清空账户
account_input.clear()
#输入用户名
account_input.send_keys("maizi_test@139.com")
#点击密码输入框
password_input =  browser.find_element_by_id("id_password_l")
#清空密码
password_input.clear()
#输入密码
password_input.send_keys("abc123456")
#点击登录
browser.find_element_by_id("login_btn").click()
