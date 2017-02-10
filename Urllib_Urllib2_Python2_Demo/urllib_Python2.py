#encoding:utf-8

"""
urllib简单用法
"""
import  urllib

class MySeachE():

    def search_urllib(self):
        baidu = urllib.urlopen('http://www.baidu.com')
        # print("################################")
        # print 'http header:/n', baidu.info()
        # print("################################")
        # print 'http status:', baidu.getcode()
        # print("################################")
        # print 'url:', baidu.geturl()
        # print("################################")

        for line in baidu: # 就像在操作本地文件
            print line
        print("################################")
        baidu.close()

if  __name__ == "__main__":
    mySeacher = MySeachE()
    mySeacher.search_urllib()