import time, threading, multiprocessing


def loop1():
    x = 0
    while True:
        print(x)
        x = x + 1


for i in range(multiprocessing.cpu_count()):
    t1 = threading.Thread(target=loop1)
    t1.start()
