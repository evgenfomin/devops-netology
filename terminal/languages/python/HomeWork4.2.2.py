#!/usr/bin/env python3
import os

os.chdir("/home/evgeniy/devops-netology/devops-netology")
adress = os.getcwd()
files_status = os.popen("git status").read()
files_mod = list()

for str in files_status.split('\n'):
    if str.find('modified') != -1:
        for word in str.split(' '):
            files_mod.append(word)
        print (f'{files_mod[0]} {adress}{files_mod[3]}')
        files_mod = list()