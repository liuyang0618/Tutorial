#encoding:utf-8
__author__ = 'Administrator'

"""
tcp接收端
"""

import  socket

#创建socket的对象
s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#绑定端口
s.bind(("",5005))

#监听端口(可以监听5个客户端的)
s.listen(5)

#接收连接
clientsock, clientaddr = s.accept()

#接收数据
data = clientsock.recv(1024)

#显示数据
print ('received msg:', data)

#向发送端发送数据
clientsock.send(data + "-收到" )

#结束
clientsock.close()