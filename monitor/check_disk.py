#!/usr/bin/env python
import os
import statvfs
import commands
War = 10
error = 20

def check_disk():
    disk = (commands.getoutput("df -lh | grep ceph | awk '{print $6}'")).split("\n")
    for line in disk:
        if line != "Filesystem":
            vfs = os.statvfs(line)
            available = vfs[statvfs.F_BFREE] * vfs[statvfs.F_BSIZE] / (1024 * 1024 * 1024)
            capacity = vfs[statvfs.F_BLOCKS] * vfs[statvfs.F_BSIZE] / (1024 * 1024 * 1024)
            used = float(capacity) - float(available)
            use_disk = (used / capacity) * 100
            if use_disk > 0 and use_disk < error:
                print "The %s warning and used: %s %%" % (line,use_disk)
            elif use_disk > error:
                print "The %s error and used: %s %% " % (line,use_disk)
            else:
                print "The %s is right and used: %s %%" % (line,use_disk)
        else:
            print "Wrong: %s " % line

if __name__ == '__main__':
    check_disk()

