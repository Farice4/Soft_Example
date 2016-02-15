import shutil
import os
import commands
import fileinput
import sys


count = 0 
Old_Message = 'notification_driver=messaging'
New_Message1 = 'notification_driver=ceilometer.compute.nova_notifier'
New_Message2 = 'notification_driver=nova.openstack.common.notifier.rpc_notifier'
New_Message3 = '#notification_driver=messaging'

#backup_file = '/etc/nova/nova.conf'

old_file = '/etc/nova/nova.conf'
backup_file = old_file + '.bak'


os.system("cp %s %s" % (old_file, backup_file))
if not os.path.exists('%s' % backup_file):
    print 'error'
    sys.exit(1)
   

f = open('%s' % old_file)

fnew = open('/root/backup.conf', 'w')

for line in f:
    if line =='%s\n' % Old_Message:
        if count == 0:
            fnew.write('%s\n' % New_Message1)
            count+=1
        if count == 1:
            fnew.write('%s\n' % New_Message2)
            count+=1
        if count == 2:
            fnew.write('%s\n' % New_Message3)
    else:
        fnew.write(line)
fnew.close()
f.close()

os.system("mv /root/backup.conf %s" % old_file)
