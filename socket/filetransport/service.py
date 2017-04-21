#!/usr/bin/env python
# _*_coding:utf-8 _*_
import socket
# 创建一个socket对象
sk = socket.socket()
# 允许连接的IP和端口
sk.bind(('127.0.0.1', 6542))
# 最大连接数
sk.listen(5)
while True:
    # 会一直阻塞，等待接收客户端的请求，如果有客户端连接会获取两个值，conn=创建的连接，address=客户端的IP和端口
    conn, address = sk.accept()
    # 客户端发送过来的文件大小
    file_size = str(conn.recv(1024),encoding="utf-8")
    # 给客户端发送已经收到文件大小
    conn.sendall(bytes("ack", encoding="utf-8"))
    # 文件大小转换成int类型
    total_size = int(file_size)
    # 创建一个默认的值
    has_recv = 0
    # 打开一个新文件，以wb模式打开
    f = open('new_file.txt', 'wb')
    # 进入循环
    while True:
        # 如果传送过来的大小等于文件总大小，那么就退出
        if total_size == has_recv:
            break
        # 接受客户端发送过来的内容
        data = conn.recv(1024)
        # 写入到文件当中
        f.write(data)
        # 现在的大小加上客户端发送过来的大小
        has_recv += len(data)
    # 关闭
    f.close()