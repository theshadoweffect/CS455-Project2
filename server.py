from socket import *
import sys, struct, timeit
s = socket(AF_INET, SOCK_STREAM)
s.bind(("0.0.0.0", 9999))
s.listen(1)
conn, addr = s.accept()
f = open("output.txt", "w")
print('Connected by', addr)
buf = 10240
stored, addr = conn.recvfrom(buf)
prevsequence = 0
data = ''
while(stored):
    conn.settimeout(20)
    stored, addr = conn.recvfrom(buf)
    print len(stored), "bytes received..."
    buffer = stored.split('\n')
    i = 0
    while i < len(buffer)-1:
        if buffer[i][0] == ":":
            data = buffer[i]
        i = i+1
        if len(data) == 1028:
            ignore, seqNum, data = data.split(":")
            print "Receiving packet", seqNum
            if prevsequence + 1 == int(seqNum):
                prevsequence = int(seqNum)
                f.write(data)
    conn.send((str(prevsequence)+":")) 
    print "Sending acknowledgement", prevsequence
conn.close()
s.close()
f.close() 

