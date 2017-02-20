#encoding:utf-8

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

#定义访问的url
url = 'http://www.maiziedu.com'
login_text = u"登录"
account = 'maizi_test@139.com'
pwd = 'abc123456'


def get_ele_times(drvier, times, func):
    return WebDriverWait(drvier, times).until(func)


def openBrowser():
    '''
    功能：打开浏览器
    return handler
    '''
    # 启动火狐浏览器
    browser = webdriver.Firefox()
    return browser

def openUrl(handler,url):
    '''
    打开url并最大化
    '''
    # 访问url
    handler.get(url)
    # 窗口最大化
    handler.maximize_window()



# def findElement(handle,**arg):
#     '''
#         查找元素
#         1. text_id:
#         2. userid
#         3. pwdid
#         4. loginid
#         return userEle, pwdEle,loginEle
#     '''
#     # 查找搜索框
#     if text_id in arg:
#         ele_login = get_ele_times
#     ele = handle.find_element_by_link_text(arg)

def login_test():


    #打开浏览器
    browser = openBrowser()

    #打开指定网页
    openUrl(browser,url)

    ele_login = get_ele_times(browser,10,lambda browser:browser.find_element_by_link_text(login_text))
    #点击登录按钮
    # findElement(browser, login_text)
    ele_login.click()
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
    try:
        browser.find_elements_by_link_text(u'改账户格式不正确')
        print("Account And Password Error")
    except:
        print("Account And Password Right")

    browser.close( )


if __name__ == '__main__':
    login_test()