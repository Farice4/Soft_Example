#!/usr/bin/env python
# Basic gethostbyaddr() example - Chapter 4 - environment.py

import sys
import socket

def getipaddrs(hostname):
    """Given a host name, perform a standard (forward) lookup and
    return a list of IP addresses for that host."""
    result = socket.getaddrinfo(hostname, None, 0, socket.SOCK_STREAM)
    return [x[4][0] for x in result]

# Calling gethostname() returns the name of the local machine
hostname = socket.gethostname()
print "Fully-qualified name:", socket.getfqdn(hostname)
try:
    print "IP address:", ", ".join(getipaddrs(hostname))
except socket.gaierror, e:
    print "Couldn't not get IP addresses:", e
