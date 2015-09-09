#!/usr/bin/env python
import socket
host = '192.168.1.50'
port = 5000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
while True:
    message = raw_input("Please input your message: ")
    if message == 'bye':
        break
    else:
        s.sendall(message)
        data = s.recv(1024)
        print data
s.close()
print 'Received',repr(data)
