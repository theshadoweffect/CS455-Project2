from socket import *
import sys, timeit
s = socket(AF_INET, SOCK_STREAM)
s.connect(("10.0.0.2", 9999))
recvd=' '
for i in xrange(0, 10, 1):
    for j in range(1000):
        try:
            data = str(i) * 1024 + '\n'
            s.send(data)
            print "Loop 1 sending", len(data), "bytes..."
            print "Loop 1 waiting for acknowledgement"
            s.settimeout(5)
	    recvd = s.recv(1)
            print ("Acknowledgement recieved", recvd)
	    break
       except TimeoutError:
	    pass
for i in xrange(ord('a'), ord('z') + 1, 1):
    for j in range(1000):
        try:
            data = chr(i) * 1024 + '\n'
            s.send(data)
            print "Loop 2 sending", len(data), "bytes..."
            print "Loop 2 waiting for acknowledgement"
            s.settimeout(5)
	    recvd = s.recv(1)
            print ("Acknowledgement recieved", recvd)
	    break
       except TimeoutError:
	    pass
for i in xrange(ord('A'), ord('Z') + 1, 1):
    for j in range(1000):
        try:
            data = chr(i) * 1024 + '\n'
            s.send(data)
            print "Loop 3 sending", len(data), "bytes..."
            print "Loop 3 waiting for acknowledgement"
            s.settimeout(5)
	    recvd = s.recv(1)
            print ("Acknowledgement recieved", recvd)
	    break
       except TimeoutError:
	    pass
s.close()
