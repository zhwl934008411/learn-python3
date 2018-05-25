# -*- coding:utf-8 -*-

import os
import time, threading, multiprocessing, datetime

# print("Process(%s) start..." % os.getppid())
# Only work on Unix/Linux/Mac:
'''pid = os.fork()
if pid == 0:
    print("I am child process (%s) and my parent id %s." % (os.getpid(), os.getppid())
#else:
    #print("I (%s) just created a child process (%s)." % (os.getpid(), pid)'''


class Multithreading(object):
    def loop(self):
        print("thread %s is running.. " % threading.current_thread().name)
        n = 0
        while n < 5:
            n = n + 1
            print('thread %s >>> %s' % (threading.current_thread().name, n))
            time.sleep(1)
        print('thread %s ended.' % threading.current_thread().name)


if __name__ == '__main__':
    mt = Multithreading()
    # 调用threading类的Thread方法，传入target,name关键参数，target=__loop__,name='LoopThread'创建实例t
    # t = threading.Thread(target=mt.loop, name='LoopThread')
    t = threading.Thread(target=mt.loop)
    t.start()
    t.join()
    # 线程threading可以看成一个类，调用类的方法创建实例
    print(datetime.datetime.now())
