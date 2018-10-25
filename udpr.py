from socket import *
import sys, struct, timeit
host = "0.0.0.0"
port = 9999
s = socket(AF_INET, SOCK_DGRAM)
s.bind((host,port))
addr = (host,port)
buf=10240
f = open("output.txt", 'w')
data, addr = s.recvfrom(buf)
s.settimeout(2)
start_time = timeit.default_timer()
try:
    while(data):
        f.write(data)
        data, addr = s.recvfrom(buf)
        print len(data), "bytes received..."
except timeout:
    f.close()
    s.close()
elapsed = (timeit.default_timer() - start_time - 2)
print '%.3f seconds' % elapsed
