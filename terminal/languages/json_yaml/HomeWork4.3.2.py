#!/usr/bin/env python3
import socket, json, yaml

ipdict = { 'drive.google.com': '', 'mail.google.com': '', 'google.com': ''}
for domain in ipdict:
    ipdict[domain] = socket.gethostbyname(domain)

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
