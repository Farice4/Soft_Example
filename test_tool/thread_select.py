#!/usr/bin/python

import threading
import time
import os
import sys
import commands

def test(max_num):
    for i in range(max_num):
        time.sleep(1)
        print "------->Start [%s]---------->" % i
        s = commands.getoutput("ceilometer sample-list -m ram_util")
        print s

threads=[]
for x in range(100):
    t=threading.Thread(target=test, args=(500, ))
    threads.append(t)

for thr in threads:
    thr.start()

for thr in threads:
    if thr.isAive():
        thr.join()
