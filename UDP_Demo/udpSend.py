# coding:utf-8
__author__ = 'ly'

"""
udp 协议的发送端
"""
import socket

# 创建socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 指定地址和端口 & 发送消息
s.sendto("Hello  world", ("192.168.98.213", 5055))

#关闭连接
s.close()

