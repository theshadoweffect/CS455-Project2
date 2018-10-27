from socket import *
import sys, struct, timeit
s = socket(AF_INET, SOCK_STREAM)
s.bind(("0.0.0.0", 9999))
s.listen(1)
conn, addr = s.accept()
start_time = timeit.default_timer()
f = open("output.txt", "w")
print('Connected by', addr)
buf = 1024
data, addr = conn.recvfrom(buf)
prevsequence = -1
packets = 1
while(data):
    conn.settimeout(10)
    seq, addr = conn.recvfrom(3)
    data, addr = conn.recvfrom(buf)
    print len(data), "bytes received..."
    packets = packets + 1
    seqNum = seq.split(":")
    print "Receiving packet", seqNum[0]
    if prevsequence + 1 == int(seqNum[0]):
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
