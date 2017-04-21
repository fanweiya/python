import threading
import time
def Princ(String):
    print('task', String)
    time.sleep(5)
# target=目标函数， args=传入的参数
t1 = threading.Thread(target=Princ, args=('t1',))
t1.start()
t2 = threading.Thread(target=Princ, args=('t1',))
t2.start()
t3 = threading.Thread(target=Princ, args=('t1',))
t3.start()

class MyThreading(threading.Thread):
    def __init__(self, conn):
        super(MyThreading, self).__init__()
        self.conn = conn
    def run(self):
        print('run task', self.conn)
        time.sleep(5)
t1 = MyThreading('t1')
t2 = MyThreading('t2')
t1.start()
t2.start()


for i in range(50):
    t = threading.Thread(target=Princ, args=('t-%s' % (i),))
    t.start()
    t.join()

# 执行子线程的时间
start_time = time.time()
# 存放线程的实例
t_objs = []
for i in range(50):
    t = threading.Thread(target=Princ, args=('t-%s' % (i),))
    t.start()
    # 为了不让后面的子线程阻塞，把当前的子线程放入到一个列表中
    t_objs.append(t)
# 循环所有子线程实例，等待所有子线程执行完毕
for t in t_objs:
    t.join()
# 当前时间减去开始时间就等于执行的过程中需要的时间
print(time.time() - start_time)

class MyThreading(threading.Thread):
    def __init__(self):
        super(MyThreading, self).__init__()
    def run(self):
        print('我是子线程： ', threading.current_thread())
t = MyThreading()
t.start()
print('我是主线程： ', threading.current_thread())


class MyThreading(threading.Thread):
    def __init__(self):
        super(MyThreading, self).__init__()
    def run(self):
        print('www.anshengme.com')
t = MyThreading()
t.start()
print('线程个数： ', threading.active_count())