from socket import *
import sys, timeit
s = socket(AF_INET, SOCK_STREAM)
s.connect(("10.0.0.2", 9999))
timeInterval = 3
s.settimeout(timeInterval)
seq = 0
lastACK = 0
curWindow = 5
N = 5
while seq <= 62:
    if seq < curWindow:
	if seq < 10:
		seqName = str(0) + str(seq)
	else:
		seqName = str(seq)
        data = seqName + ":" + str(1) * 1024 + '\n'
        s.send(data)
        print "Sequence: ", seqName, "sending", len(data), "bytes..."
        seq = seq + 1
    if seq == curWindow:
        try:
            data, addr = s.recvfrom(1024)
	    array = data.split(":")
	    ACK = int(array[-1:])
	    curWindow = N + ACK
	    seq = ACK+1
	    print ("Acknowledgement recieved", ACK)
        except timeout:
	    seq = curWindow - N
s.close()
