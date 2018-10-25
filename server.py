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
while(data):
    conn.settimeout(2)
    data, addr = conn.recvfrom(buf)
    print len(data), "bytes received..."
    f.write(data);
    conn.send("A")
print "Sending acknowledgement"
conn.close()
s.close()
f.close()
elapsed = (timeit.default_timer() - start_time)
print '%.3f seconds' % elapsed
