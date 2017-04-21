def consumer(name):
    print("--->starting eating baozi...")
    while True:
        new_baozi = yield  # 直接返回
        print("[%s] is eating baozi %s" % (name, new_baozi))
def producer():
    r = con.__next__()
    r = con2.__next__()
    n = 0
    while n < 5:
        n += 1
        con.send(n)  # 唤醒生成器的同时传入一个参数
        con2.send(n)
        print("\033[32;1m[producer]\033[0m is making baozi %s" % n)
if __name__ == '__main__':
    con = consumer("c1")
    con2 = consumer("c2")
    p = producer()


from greenlet import greenlet
def func1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()
def func2():
    print(56)
    gr1.switch()
    print(78)
# 创建两个协程
gr1 = greenlet(func1)
gr2 = greenlet(func2)
gr1.switch()  # 手动切换

import gevent
def foo():
    print('Running in foo')
    gevent.sleep(2)
    print('Explicit context switch to foo again')
def bar():
    print('Explicit context to bar')
    gevent.sleep(3)
    print('Implicit context switch back to bar')
# 自动切换
gevent.joinall([
    gevent.spawn(foo),  # 启动一个协程
    gevent.spawn(bar),
])

from urllib import request
from gevent import monkey
import gevent
import time
monkey.patch_all()  # 当前程序中只要设置到IO操作的都做上标记
def wget(url):
    print('GET: %s' % url)
    resp = request.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))
urls = [
    'https://www.python.org/',
    'https://www.python.org/',
    'https://github.com/',
    'https://blog.ansheng.me/',
]
# 串行抓取
start_time = time.time()
for n in urls:
    wget(n)
print("串行抓取使用时间：", time.time() - start_time)
# 并行抓取
ctrip_time = time.time()
gevent.joinall([
    gevent.spawn(wget, 'https://www.python.org/'),
    gevent.spawn(wget, 'https://www.python.org/'),
    gevent.spawn(wget, 'https://github.com/'),
    gevent.spawn(wget, 'https://blog.ansheng.me/'),
])
print("并行抓取使用时间：", time.time() - ctrip_time)
