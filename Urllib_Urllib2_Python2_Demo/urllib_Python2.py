#encoding:utf-8

"""
urllib简单用法
此模块的作用是打开任意的url

urllib模块中的方法:
1.urllib.urlopen(url[,data[,proxies]])
打开一个url的方法，返回一个文件对象，然后可以进行类似文件对象的操作。

2.urllib.urlretrieve(url[,filename[,reporthook[,data]]])
urlretrieve方法将url定位到的html文件下载到你本地的硬盘中。如果不指定filename，则会存为临时文件。
urlretrieve()返回一个二元组(filename,mine_hdrs)

"""
import  urllib

class MySeachE():

    def search_urllib_urlopen(self):

        #打开url
        baidu = urllib.urlopen('http://www.baidu.com')
        # urlopen返回对象提供方法：
        # -         read() , readline() ,readlines() , fileno() , close() ：这些方法的使用方式与文件对象完全一样
        # -         info()：返回一个httplib.HTTPMessage对象，表示远程服务器返回的头信息
        # -         getcode()：返回Http状态码。如果是http请求，200请求成功完成;404网址未找到
        # -         geturl()：返回请求的url

        # print("################################")
        # #获取请求资源的请求头
        # print 'http header:/n', baidu.info()
        #
        # print("################################")
        # #获取请求的状态码
        # print 'http status:', baidu.getcode()
        #
        #
        # print("################################")
        # # 获取实际请求的url
        # print 'url:', baidu.geturl()
        #
        # print("################################")
        # #逐行打印返回的信息
        # for line in baidu: # 就像在操作本地文件
        #     print line
        # print("################################")

        #返回对象的read()：读取全部
        # resp = baidu.read()
        # print resp

        #readline()：读取一行
        # resp = baidu.readline()
        # print resp

        # #readlines() ：读取所有行，返回的是一个list
        # resp = baidu.readlines()
        # # print resp
        # for line in resp:
        #     print line

        #fileno(): 返回文件内容的长度
        # resp = baidu.fileno()
        # print resp

        baidu.close()

    def search_urllib_urlretrieve(self):
        #返回一个元祖
        baidu = urllib.urlretrieve("http://www.baidu.com/",filename="baidu.html")
        print (baidu[0],baidu[1])


if  __name__ == "__main__":
    mySeacher = MySeachE()
    # mySeacher.search_urllib_urlopen()
    mySeacher.search_urllib_urlretrieve()