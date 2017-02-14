#encoding:utf-8

"""
urllib2常用使用方法介绍

"""
import urllib2
import cookielib

class MySearchE():
    """
    Proxy 的设置
    Timeout 设置
    在 HTTP Request 中加入特定的 Header
    Redirect
    Cookie
    使用 HTTP 的 PUT 和 DELETE 方法
    得到 HTTP 的返回码
    Debug Log
    """

    #代理设置
    def urlli2_ProxyHandler(self):

        enable_proxy = True
        proxy_handler = urllib2.ProxyHandler({"http": 'http://some-proxy.com:8080'})
        null_proxy_handler = urllib2.ProxyHandler({})

        if enable_proxy:
            opener = urllib2.build_opener(proxy_handler)
            print "yes"
        else:
            opener = urllib2.build_opener(null_proxy_handler)
            print "no"

        #urllib2全局使用代理
        urllib2.install_opener(opener)
        #urllib2.urlopen()

        #仅限次代理对象使用此代理
        #opener.open()

    #请求url并设置超时
    def urllib2_urlopen(self):
        #打开任意资源url，同urllib.urlopen，只是请求参数不同
        response = urllib2.urlopen('http://www.baidu.com', timeout=10)
        print(response.geturl())
        print(response.getcode())
        print(response.info())
        print(response.read())

    #加入特定的header
    def urllib2_Request(self):
        request = urllib2.Request("http://www.baidu.com")

        """
        User-Agent : 有些服务器或 Proxy 会通过该值来判断是否是浏览器发出的请求
        Content-Type : 在使用 REST 接口时，服务器会检查该值，用来确定 HTTP Body 中的内容该怎样解析。常见的取值有：
            application/xml ： 在 XML RPC，如 RESTful/SOAP 调用时使用
            application/json ： 在 JSON RPC 调用时使用
            application/x-www-form-urlencoded ： 浏览器提交 Web 表单时使用
            在使用服务器提供的 RESTful 或 SOAP 服务时， Content-Type 设置错误会导致服务器拒绝服务
        """
        request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36')
        response = urllib2.urlopen(request)
        #查看头信息
        print response.info()

    # 重定向
    def urllib2_Redirect(self):
        #判断是否重定向（默认如果出现301自动会重定向的）
        response = urllib2.urlopen('http://http://www.baidu.com')
        redirected = response.geturl() == 'http://www.baidu.com'

        #如果不想执行默认重定向则可以自定义HTTPRedirectHandler类并重写对应的方法
        """
        class RedirectHandler(urllib2.HTTPRedirectHandler):
            def http_error_301(self, req, fp, code, msg, headers):
                pass

            def http_error_302(self, req, fp, code, msg, headers):
                pass

        opener = urllib2.build_opener(RedirectHandler)
        opener.open('http://www.google.cn')
        """
    def urllib2_getCookie(self):
        cookie = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        response = opener.open('http://www.baidu.com')
        for item in cookie:
            if item.name == 'BAIDUID':
                print item.value

    def urllib2_getDebugLog(self):
        # 开启调试日志：通过调试日志我们可以看到User-Agent: Python-urllib/2.7
        httpHandler = urllib2.HTTPHandler(debuglevel=1)
        httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
        opener = urllib2.build_opener(httpHandler, httpsHandler)

        urllib2.install_opener(opener)
        response = urllib2.urlopen('http://www.baidu.com')


if __name__ == "__main__":
    searcher = MySearchE()
    # 代理设置
    # searcher.urlli2_ProxyHandler()
    # 请求url并设置超时
    searcher.urllib2_urlopen()
    # 加入特定的header
    searcher.urllib2_Request()
    # 获取cookie
    searcher.urllib2_getCookie()
    #获取调试日志
    searcher.urllib2_getDebugLog()