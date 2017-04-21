#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import socket
# 创建一个socket对象
sk = socket.socket()
# 绑定允许连接的IP地址和端口
sk.bind(('127.0.0.1', 6254, ))
# 服务端允许起来之后，限制客户端连接的数量，如果超过五个连接，第六个连接来的时候直接断开第六个。
sk.listen(5)
print("正在等待客户端连接....")
# 会一直阻塞，等待接收客户端的请求，如果有客户端连接会获取两个值，conn=创建的连接，address=客户端的IP和端口
conn, address = sk.accept()
# 输入客户端的连接和客户端的地址信息
print(address, conn)