
#!/usr/bin/env python3
from scapy.all import *

a = IP() 
a.dst = '8.8.8.8'
a.ttl = 1, 15

b = ICMP() 
ans, unans = sr(a/b, timeout = 2)
for snd, rcv in ans:
    print(snd.ttl, rcv.src, isinstance(rcv.payload, ICMP))
    
    if(rcv.src == a.dst):
        break

print("Traceroute Complete.")