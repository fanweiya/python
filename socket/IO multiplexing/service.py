#!/usr/bin/env python
# _*_coding:utf-8 _*_
import select
import socket
sk1 = socket.socket()
sk1.bind(('127.0.0.1', 8002, ))
sk1.listen()
demo_li = [sk1]
outputs = []
message_dict = {}
while True:
    r_list, w_list, e_list = select.select(sk1, outputs, [], 1)
    print(len(demo_li),r_list)
    for sk1_or_conn in r_list:
        if sk1_or_conn == sk1:
            conn, address = sk1_or_conn.accept()
            demo_li.append(conn)
            message_dict[conn] = []
        else:
            try:
                data_bytes = sk1_or_conn.recv(1024)
                # data_str = str(data_bytes, encoding="utf-8")
                # print(data_str)
                # sk1_or_conn.sendall(bytes(data_str+"good", encoding="utf-8"))
            except Exception as e:
                demo_li.remove(sk1_or_conn)
            else:
                data_str = str(data_bytes, encoding="utf-8")
                message_dict[sk1_or_conn].append(data_str)
                outputs.append(sk1_or_conn)
    for conn in w_list:
        recv_str = message_dict[conn][0]
        del message_dict[conn][0]
        conn.sendall(bytes(recv_str+"Good", encoding="utf-8"))
        outputs.remove(conn)