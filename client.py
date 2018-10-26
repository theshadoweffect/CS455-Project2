from socket import *
import sys, timeit
s = socket(AF_INET, SOCK_STREAM)
s.connect(("10.0.0.2", 9999))
s.settimeout(0.5)
seq = 0
curWindow = 5
N = 5
for i in xrange(0, 10, 1):
    if seq < curWindow:
        data = str(seq) + str(i) * 1024 + '\n'
        s.send(data)
        print "Loop 1 sending", len(data), "bytes..."
        seq = seq + 1
    recieved = False
    else:
        while not recieved:	
            try:
                ACK, addr = s.recvfrom(1024)
                print ("Acknowledgement recieved", ACK)
	        curWindow = N + ACK
	        seq = ACK + 1
		i = seq
	        recieved = True
            except timeout:
		seq = curWindow - N
		i = seq
for i in xrange(ord('a'), ord('z') + 1, 1):
    if seq < curWindow:
        data = str(seq) + chr(i) * 1024 + '\n'
        s.send(data)
        print "Loop 1 sending", len(data), "bytes..."
        seq = seq + 1
    recieved = False
    else:
        while not recieved:	
            try:
                ACK, addr = s.recvfrom(1024)
                print ("Acknowledgement recieved", ACK)
	        curWindow = N + ACK
	        seq = ACK + 1
		i = seq
	        recieved = True
            except timeout:
		seq = curWindow - N
		i = seq
for i in xrange(ord('A'), ord('Z') + 1, 1):
    if seq < curWindow:
        data = str(seq) + chr(i) * 1024 + '\n'
        s.send(data)
        print "Loop 1 sending", len(data), "bytes..."
        seq = seq + 1
    recieved = False
    else:
        while not recieved:	
            try:
                ACK, addr = s.recvfrom(1024)
                print ("Acknowledgement recieved", ACK)
	        curWindow = N + ACK
	        seq = ACK + 1
		i = seq
	        recieved = True
            except timeout:
		seq = curWindow - N
		i = seq
s.close()
