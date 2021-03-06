#!/usr/bin/env python3
import socket
dnsdrivegoogle = 'drive.google.com'
dnsmailgoogle = 'mail.google.com'
dnsgoogle = 'google.com'
ipdrivegoogle = socket.gethostbyname(dnsdrivegoogle)
ipmailgoogle = socket.gethostbyname(dnsmailgoogle)
ipgoogle = socket.gethostbyname(dnsgoogle)

ipdict = { dnsdrivegoogle: ipdrivegoogle, dnsmailgoogle: ipmailgoogle, dnsgoogle: ipgoogle}
a=0

while a < 10:
    for i in ipdict:
        if socket.gethostbyname(i) == ipdict[i]:
            print(f'{i} = {ipdict[i]}')
        else:
            print(f'[ERROR] {i} = {ipdict[i]}')
    a += 1
