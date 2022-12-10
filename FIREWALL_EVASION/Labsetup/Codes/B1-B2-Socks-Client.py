#!/bin/env python3

import socks

skt = socks.socksocket()

# Set up the proxy
skt.set_proxy(socks.SOCKS5, "192.168.20.99", 8000) 

# Connect to final destination with the help of the proxy
host = "www.example.com"
skt.connect((host, 80))

req = b"GET / HTTP/1.0\r\nHost: " + host.encode('utf-8') + b"\r\n\r\n"
skt.sendall(req)

# Get the response
res = skt.recv(2048)
while res:
    print(response.split(b"\r\n"))
    response = skt.recv(2048)
