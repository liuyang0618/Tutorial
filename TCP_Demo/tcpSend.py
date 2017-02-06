#coding:utf-8
__author__ = 'Administrator'

import  socket

#创建socket对象(tcp类型)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#指定连接的地址和端口号
addr = "192.168.98.213"
port = 5055

#连接接收端
s.connect((addr, port))

#发送数据
s.send("Hello world")

#等待接收端返回数据
data = s.recv(1024)

#显示接收端返回的数据
print('received sendback', data)

#结束
s.close()





