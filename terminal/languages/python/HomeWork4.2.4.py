#!/usr/bin/env python3
import socket
dns_name1 = 'drive.google.com'
dns_name2 = 'mail.google.com'
dns_name3 = 'google.com'
ipadress1_new = str
ipadress1_old = socket.gethostbyname(dns_name1)
ipadress2_new = str
ipadress2_old = socket.gethostbyname(dns_name2)
ipadress3_new = str
ipadress3_old = socket.gethostbyname(dns_name3)
a = 0
while(a < 10):
    ipadress1_new = socket.gethostbyname(dns_name1)
    if ipadress1_new == ipadress1_old:
        print ( f'{dns_name1} {ipadress1_old}')
    else:
        print (f'[ERROR] {dns_name1} IP mismatch:{ipadress1_old} {ipadress1_new}')

    ipadress2_new = socket.gethostbyname(dns_name2)
    if ipadress2_new == ipadress2_old:
        print ( f'{dns_name2} {ipadress2_old}')
    else:
        print (f'[ERROR] {dns_name2} IP mismatch:{ipadress2_old} {ipadress2_new}')

    ipadress3_new = socket.gethostbyname(dns_name3)
    if ipadress3_new == ipadress3_old:
        print ( f'{dns_name3} {ipadress3_old}')
    else:
        print (f'[ERROR] {dns_name3} IP mismatch:{ipadress3_old} {ipadress3_new}')



    a += 1