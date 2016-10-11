# -*- coding: utf-8 -*-
# This script use configure ceilometer.conf mongodb ip

import sys
import os
import commands
import pymongo
from pymongo import MongoClient

# Use pymongo MongoClient get mongo member ip message,
# mongodb has replica set or one node status
try:
    ss = MongoClient("mongodb://admin:%s@%s/admin" % (sys.argv[2],
                     sys.argv[1])).admin.command("isMaster")["hosts"]
except KeyError:
    ip = sys.argv[1]
    ss = []
    ss.append(ip)
except pymongo.errors.ConfigurationError:
    sys.exit("parameter error,maybe password error")
except pymongo.errors.ConnectionFailure:
    sys.exit("database connection error,maybe ip address connection error")

# Change list to str
d_ip = ",".join(ss)

# Get ceilometer.conf database connection configure
(s, o) = commands.getstatusoutput("cat /etc/ceilometer/ceilometer.conf |grep '^connection=mongodb'|cut -d@ -f 2|cut -d/ -f 1")

if s != 0 or o is None:
    sys.exit()
else:
    s_ip = o

input_file = open('/etc/ceilometer/ceilometer.conf')
output_file = open('/tmp/ceilometer_new.conf', 'w')

# when mongodb get ip, ceilometer.conf connection ip the same,
# the configure nothing to do,  if not same touch output file
for s in input_file:
    if s_ip == d_ip:
        pass
    else:
        output_file.write(s.replace(s_ip, d_ip))

output_file.close()
input_file.close()

if os.path.getsize('/tmp/ceilometer_new.conf') > 0:
    os.rename('/etc/ceilometer/ceilometer.conf',
              '/etc/ceilometer/ceilometer_old.conf')
    os.rename('/tmp/ceilometer_new.conf',
              '/etc/ceilometer/ceilometer.conf')
    commands.getoutput('systemctl restart openstack-ceilometer-collector httpd')
else:
    sys.exit()
