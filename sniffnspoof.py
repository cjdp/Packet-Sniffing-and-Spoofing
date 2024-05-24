#!/usr/bin/env python3

from scapy.all import *

def spoof_packet(pkt):
    # only check for echo
    if pkt[ICMP].type != 8:
        return
    count = 0

    #insert sniffed ping packets information into spoof_packet's field
    ip = IP(src = pkt[IP].dst, dst = pkt[IP].src, ihl = pkt[IP].ihl)
    icmp = ICMP (type = 0, id = pkt[ICMP].id, seq = pkt[ICMP].seq)
    data  = pkt[Raw].load
    newpkt = ip/icmp/data

    send(newpkt, verbose = 0)
    count += 1

    print("Spoofed Packet Sent.")