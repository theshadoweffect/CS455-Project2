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
        if int(checkBuf[0]) - 1 == int(data[0]):
            checkBuf.pop(0)
            data.pop(0)
            f.write(data)
            f.write(checkBuf)
        else:
            data.pop(0)
            f.write(data)
    else:
        checkBuf = data
    conn.send(prevsequence) 
print "Sending acknowledgement"
conn.close()
s.close()
f.close()
elapsed = (timeit.default_timer() - start_time)
print '%.3f seconds' % elapsed
