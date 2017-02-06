# coding:utf-8
__author__ = 'ly'

"""
udp 协议的接收端
"""
import socket

# 创建socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口
s.bind(("", 5055))

#接收消息
data, address = s.recvfrom(1024)

#打印接收的信息
print 'receive   msg: %s' % data

#关闭连接
s.close()



