from socket import *
import sys
s = socket(AF_INET,SOCK_DGRAM)
host = "10.0.0.2"
port = 9999
addr = (host, port)
for i in xrange(0, 10, 1):
    data = str(i) * 1024 + '\n'
    s.sendto(data, addr)
    print "sending", len(data), "bytes..."
for i in xrange(ord('a'), ord('z') + 1, 1):
    data = chr(i) * 1024 + '\n'
    s.sendto(data, addr)
    print "sending", len(data), "bytes..."
for i in xrange(ord('A'), ord('Z') + 1, 1):
    data = chr(i) * 1024 + '\n'
    s.sendto(data, addr)
    print "sending", len(data), "bytes..."
s.close()
