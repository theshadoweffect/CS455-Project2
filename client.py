from socket import *
import sys, timeit
s = socket(AF_INET, SOCK_STREAM)
s.connect(("10.0.0.2", 9999))
s.settimeout(2)
seq = 0
curWindow = 5
N = 5
a = ":"
while seq < 62:
    if seq < curWindow:
        data = str(seq) + str(a) + str(1) * 1024 + '\n'
        s.send(data)
        print "Sequence: ", seq, "sending", len(data), "bytes..."
        seq = seq + 1	
    try:
        ACK, addr = s.recvfrom(1024)
        print ("Acknowledgement recieved", ACK)
	ACK = int(ACK)
	curWindow = N + ACK
	seq = ACK + 1
	i = seq
    except timeout:
	seq = curWindow - N
s.close()
