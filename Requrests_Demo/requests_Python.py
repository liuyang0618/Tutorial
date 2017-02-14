#encoding:utf-8

"""
requests模块
requests是Python的一个HTTP客户端库，跟urllib，urllib2类似，那为什么要用requests而不用urllib2呢？官方文档中是这样说明的：
python的标准库urllib2提供了大部分需要的HTTP功能，但是API太逆天了，一个简单的功能就需要一大堆代码。
-->原因：
    1. 简单       2.Python2&Python3通用

"""
import requests


def send_getRequest():
    #发送get请求
    req = requests.get('http://www.baidu.com')
    #返回码
    print req.status_code
    #返回头信息
    print req.headers['content-type']
    #返回内容(以字节的方式去显示)
    print req.content
    #返回编码
    print req.encoding

    payload = {'wd': '张亚楠', 'rn': '100'}
    r = requests.get("http://www.baidu.com/s", params=payload)
    print type(r)
    print r.url

    #头完整信息
    print r.headers


    r1 = requests.get('http://ip.taobao.com/service/getIpInfo.php?ip=122.88.60.28')
    #以json的格式显示
    print type(r1.content)
    print r1.content


#发送post请求
def send_postRequest():
    url = 'http://127.0.0.1:8080/test'
    datas = {
        'aaa' : 'bbb'
    }
    headers = {
        'Authorization' : 'xxxxxx'
    }
    ret = requests.get(url, datas, headers=headers)
    print ret

#发送其他请求
def send_otherRequest():
    pass

#代理
def send_request_proxy():
    proxies = {
        "http": "http://10.10.1.10:3128",
        "https": "http://10.10.1.10:1080",
    }

    requests.get("http://www.zhidaow.com", proxies=proxies)

if __name__ == "__main__" :
    send_getRequest()
    #send_postRequest()
    # send_otherRequest()
    send_request_proxy()

