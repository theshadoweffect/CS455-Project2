from socket import *
import sys, timeit
s = socket(AF_INET, SOCK_STREAM)
s.connect(("10.0.0.2", 9999))
s.settimeout(0.5)
for i in xrange(0, 10, 1):
    data = str(i) * 1024 + '\n'
    s.send(data)
    acknowledged = False
    while not acknowledged
        try:
	    ACK, addr = s.recvfrom(1024)
            print ("Acknowledgement recieved", recvd)
            acknowledged = True
        except s.timeout:
	    s.send(data)
for i in xrange(ord('a'), ord('z') + 1, 1):
    data = chr(i) * 1024 + '\n'
    s.send(data)
    print "Loop 2 sending", len(data), "bytes..."
    print "Loop 2 waiting for acknowledgement"
    acknowledged = False
    while not acknowledged
        try:
	    ACK, addr = s.recvfrom(1024)
            print ("Acknowledgement recieved", recvd)
            acknowledged = True
        except s.timeout:
	    s.send(data)
for i in xrange(ord('A'), ord('Z') + 1, 1):
    acknowledged = False
    while not acknowledged
        try:
	    ACK, addr = s.recvfrom(1024)
            print ("Acknowledgement recieved", recvd)
            acknowledged = True
        except s.timeout:
	    s.send(data)
s.close()
