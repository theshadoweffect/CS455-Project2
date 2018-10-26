from socket import *
import sys, struct, timeit
s = socket(AF_INET, SOCK_STREAM)
s.bind(("0.0.0.0", 9999))
s.listen(1)
conn, addr = s.accept()
start_time = timeit.default_timer()
f = open("output.txt", "w")
print('Connected by', addr)
buf = 10240
data, addr = conn.recvfrom(buf)
prevsequence = -1
while(data):
    conn.settimeout(5)
    data, addr = conn.recvfrom(buf)
    print len(data), "bytes received..."
    c = data[0]
    seqNum = ""
    while c != ":":
        seqNum.push(c)
        temp = data[-1]
        data = data[:-1]
        c = data[0]
    temp = data[-1]
    data = data[:-1]
    if data.len == 1025:
        print "Receiving packet", seqNum
        if prevsequence + 1 == int(seqNum):
            prevsequence = int(seqNum)
            f.write(data)
    conn.send(str(prevsequence)) 
    print "Sending acknowledgement", prevsequence
conn.close()
s.close()
f.close()
elapsed = (timeit.default_timer() - start_time)
print '%.3f seconds' % elapsed
