#!/usr/bin/python
import thread
import time
import os

count = 600

def test(threadName):
    print "%s enter" % (threadName)
    os.system('ceilometer sample-list -m cpu_util -q "resource_id=49eb4ed6-9c2d-4f0e-a45f-f7e252ab7e1d" -l 1')
    global count
    count -= 1
    print "%s exit:%d" % (threadName, count)

for i in range(count):
    try:
        thread.start_new_thread(test, (str(i), ))
    except:
        print "Error: unable to start thread"

while 1:
    time.sleep(1000)
