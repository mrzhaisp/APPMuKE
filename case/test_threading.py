#! /usr/bin/env python
#coding=utf-8
#author=zgd
import threading
def sun(a):
    print(a+1)
threads = []

for i in range(3):
    t = threading.Thread(target=sun,args=(i,))
    threads.append(t)

for j in threads:
    j.start()









