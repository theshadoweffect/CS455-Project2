from socket import *
import sys, timeit
s = socket(AF_INET, SOCK_STREAM)
s.connect(("10.0.0.2", 9999))
timeInterval = 5
s.settimeout(timeInterval)
seq = 1
lastACK = 0
curWindow = 5
N = 5
packets = 0
while seq <= 63:
    if seq < curWindow:
	if seq < 10:
		seqName = str(0) + str(seq)
	else:
		seqName = str(seq)
        data = ":" + seqName + ":" + str(1) * 1024 + '\n'
        s.send(data)
	packets+1
        print "Sequence: ", seqName, "sending", len(data), "bytes..."
        seq = seq + 1
    if seq == curWindow:
        try:
            data, addr = s.recvfrom(1024)
	    array = data.split(":")
	    last = len(array)-2
	    ACK = array[last]
	    ACK = int(ACK)
	    curWindow = N + ACK
	    seq = ACK+1
	    print ("Acknowledgement recieved", ACK)
        except timeout:
	    seq = curWindow - N
print "Loss rate:", (100 - 100*62/packets) 
s.close()
