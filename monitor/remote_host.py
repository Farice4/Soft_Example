#!/usr/bin/env python
#coding: *-* utf8 *-*
import socket
import re
import urllib2

# use socket lib to get hostname or host IP address
def get_remote_machine_info():
    remote_host = raw_input("Please input Your site name: ")
    try:
        print "IP address: %s" % socket.gethostbyname(remote_host)
        return socket.gethostbyname(remote_host)
    except socket.error, err_msg:
        print "%s: %s" %(remote_host,err_msg)

#This across IP138 query IP Localtion
class ip138:
    def __init__(self,ip):
        self.ip= ip
    def __open(self):
        return urllib2.urlopen('http://ip138.com/ips138.asp?ip='+self.ip +'&action=2')
    def __recompile(self):
        return re.compile(r'.*<li>(.*)</li><li>(.*)</li>.*')
    def get(self):
        p = self.__recompile()
        lines = self.__open()
        for line in lines:
            if '<ul class="ul1">' in line:
                return p.sub(r'\1\n\2',line).decode('gbk')

ip = socket.gethostbyname(get_remote_machine_info())  #IP use get_remote_mache_info get ip address


if __name__ == '__main__':
    m = ip138(ip)
    print "Query IP: %s\n%s" %(ip,m.get())
