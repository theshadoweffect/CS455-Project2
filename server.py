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
packets = 1
while(data):
    conn.settimeout(5)
    data, addr = conn.recvfrom(buf)
    print len(data), "bytes received..."
    packet = packet + 1
    if len(data) <= 1028 and len(data) != 0:
        seqNum, data = data.split(":")
        print "Receiving packet", seqNum
        if prevsequence + 1 == int(seqNum):
            prevsequence = int(seqNum)
            f.write(data)
    conn.send(str(prevsequence)) 
    print "Sending acknowledgement", prevsequence
droprate =  100 - (100 * 62/packets)  
print "Packet loss rate", droprate
conn.close()
s.close()
f.close()
elapsed = (timeit.default_timer() - start_time)
print '%.3f seconds' % elapsed
print '%.3f seconds' % elapsed/packets
