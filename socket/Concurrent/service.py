#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import socketserver
class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        conn.sendall(bytes("你好，欢迎登陆！", encoding="utf-8"))
        while True:
            # 输出等待客户端发送内容
            print("正在等待Client输入内容......")
            # 接收客户端发送过来的内容
            ret_bytes = conn.recv(1024)
            # 转换成字符串类型
            ret_str = str(ret_bytes, encoding="utf-8")
            # 输出用户发送过来的内容
            print(ret_str)
            # 如果用户输入的是q
            if ret_str == "q":
                # 则退出循环，等待下个用户输入
                break
            # 给客户端发送内容
            inp = input("Service请输入要发送的内容>>> ")
            conn.sendall(bytes(inp, encoding="utf-8"))
if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 999, ), MyServer)
    server.serve_forever()