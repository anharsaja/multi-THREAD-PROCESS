import time
from threading import Thread

def f1():
    for i in range(10):
        print(i, "On F1")
        time.sleep(0.75)

def f2():
    for i in range(5):
        print(i, "On F2")
        time.sleep(0.75)


t1 = Thread(target=f1)
t2 = Thread(target=f2)

t1.start()
t2.start()