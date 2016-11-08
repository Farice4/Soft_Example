#!/usr/bin/env python
# Revised Connection Example - Chapter 2 - connect_fine_port.py

import socket

print "Creating socket..."
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "done..."

print "Lokking up port number...",
port = socket.getservbyname('http', 'tcp')
print "done."

print "Connecting to remote host on port %d..." % port,
s.connect(("www.baidu.com", port ))
s.close()
print "done."
