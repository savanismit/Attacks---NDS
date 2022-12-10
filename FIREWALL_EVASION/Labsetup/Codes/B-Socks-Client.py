#!/bin/env python3

import socks

skt = socks.socksocket()

# Set up the proxy
skt.set_proxy(socks.SOCKS5, "0.0.0.0", 8000) 

# Connect to final destination with the help of proxy
host = "www.example.com"
skt.connect((host, 80))

req = b"GET / HTTP/1.0\r\nHost: " + host.encode('utf-8') + b"\r\n\r\n"
skt.sendall(req)

# Get the response
res = s.recv(2048)
while res:
    print(res.split(b"\r\n"))
    res = s.recv(2048)
