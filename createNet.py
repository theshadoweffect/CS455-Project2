#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel, info
from mininet.cli import CLI

class SingleSwitchTopo( Topo ):
    "Single switch connected to n hosts."
    def build( self, n=2 ):
	switch = self.addSwitch( 's1' )
	for h in range(n):
	    # Each host gets 50%/n of system CPU
	    host = self.addHost( 'h%s' % (h + 1),
		                 cpu=.5/n )
	    # 10 Mbps, 5ms delay, 2% loss, 1000 packet queue
	    self.addLink( host, switch, bw=1, delay='20ms', loss=10,
                          max_queue_size=10000, use_htb=True )

def test():
    "Create network and run simple performance test"
    topo = SingleSwitchTopo()
    net = Mininet( topo=topo,
	           host=CPULimitedHost, link=TCLink )
    info( 'Starting network\n' )
    net.start()
    print "Dumping host connections"
    dumpNodeConnections( net.hosts )
    print "Testing network connectivity"
    net.pingAll()
    info( 'Running CLI\n')
    CLI( net )
    info( 'Stoping network\n' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    test()
