#!/usr/bin/env python3
import os, sys
from subprocess import call, STDOUT


adress = sys.argv[1]
os.chdir(adress)

if call(["git", "status"], stderr=STDOUT, stdout=open(os.devnull, 'w')) != 0:
    print("Указаный вами адрес не является локальным репозиторием")
    exit(1)

files_status = os.popen("git status").read()
files_mod = list()

for str in files_status.split('\n'):
    if str.find('modified') != -1:
        for word in str.split(' '):
            files_mod.append(word)
        print (f'{files_mod[0]} {adress}{files_mod[3]}')
        files_mod = list()