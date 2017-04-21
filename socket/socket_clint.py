#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import socket
# 创建一个socket对象
obj = socket.socket()
# 制定服务端的IP地址和端口
obj.connect(('127.0.0.1', 6254, ))
# 连接完成之后关闭链接
obj.close()