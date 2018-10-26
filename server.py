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
checkBuf = 10240
data, addr = conn.recvfrom(buf)
prevsequence = -1
while(data):
    conn.settimeout(5)
    data, addr = conn.recvfrom(buf)
    print len(data), "bytes received..."
    if prevsequence + 1 == int(data[0]):
        prevsequence = int(data[0])
        packet = data[-1]
        data = data[:-1]
        f.write(packet)
    conn.send(str(prevsequence)) 
print "Sending acknowledgement"
conn.close()
s.close()
f.close()
elapsed = (timeit.default_timer() - start_time)
print '%.3f seconds' % elapsed
