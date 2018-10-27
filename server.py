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
prevsequence = 0
packets = 1
while(data):
    conn.settimeout(10)
    stored, addr = conn.recvfrom(buf)
    print len(data), "bytes received..."
    i = 0
    while i < 1028 and len(stored) > 0:
        data[i] = stored[0]
        stored = stored[1:]
        i=i+1
    if data == 1028:
        seqNum, data = data.split(":")
        print "Receiving packet", seqNum, "seq", int(seqNum)
        if prevsequence + 1 == int(seqNum):
            prevsequence = int(seqNum)
            f.write(data)
    conn.send((str(prevsequence)+":")) 
    print "Sending acknowledgement", prevsequence
conn.close()
s.close()
f.close()
droprate =  100 - (100 * 62/packets)  
print "Packet loss rate", droprate, "%"
elapsed = (timeit.default_timer() - start_time)
throughput = (timeit.default_timer() - start_time)/packets
print '%.3f seconds' % elapsed
print '%.3f seconds' % throughput
