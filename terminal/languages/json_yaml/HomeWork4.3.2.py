#!/usr/bin/env python3
import socket
import json
import yaml

dnsdrivegoogle = 'drive.google.com'
dnsmailgoogle = 'mail.google.com'
dnsgoogle = 'google.com'
ipdrivegoogle = socket.gethostbyname(dnsdrivegoogle)
ipmailgoogle = socket.gethostbyname(dnsmailgoogle)
ipgoogle = socket.gethostbyname(dnsgoogle)

ipdict = { dnsdrivegoogle: ipdrivegoogle, dnsmailgoogle: ipmailgoogle, dnsgoogle: ipgoogle}
with open('server.json', 'w') as js:
    js.write(json.dumps(ipdict, indent=2))

with open('server.yml', 'w') as ym:
    ym.write(yaml.dump(ipdict, indent=2))
a=0

while a < 10:
    for i in ipdict:
        if socket.gethostbyname(i) == ipdict[i]:
            print(f'{i} = {ipdict[i]}')
        else:
            print(f'[ERROR] {i} = {ipdict[i]}')
            ipdict[i] = socket.gethostbyname(i)
            with open('server.json', 'w') as js:
                js.write(json.dumps(ipdict, indent=2))

            with open('server.yml', 'w') as ym:
                ym.write(yaml.dump(ipdict, indent=2))
    a += 1
