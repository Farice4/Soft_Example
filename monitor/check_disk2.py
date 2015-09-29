#!/usr/bin/env python
import commands
war = 10
error = 15
def check_ceph_disk():
    disk_use = commands.getoutput("ceph df | grep '%RAW USED' -A 1 | awk '{print $4}'")
    dk = float((disk_use.split("USED\n"))[1])
    if dk > 0 and dk < war:
        print "The ceph cluster space used is Right , and The space is : %s %% " % dk
    elif dk > war and dk < error:
        print "The ceph cluster space used is warning, and The space is : %s %% " % dk
    else:
        print "The ceph cluster space used is ERROR, and The space is : %s %% " % dk
if __name__ == '__main__':
    check_ceph_disk()
