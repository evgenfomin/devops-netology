1 \
ansible-playbook playbook/site.yml -i playbook/inventory/test.yml 
```
TASK [Print fact] *************************************************************************************************************************************************************
ok: [localhost] => {
    "msg": 12
}
```
2 \
```
TASK [Print fact] *************************************************************************************************************************************************************
ok: [localhost] => {
    "msg": "all default fact"
}
```
3 \
Запустил два контейнера
```
docker ps
CONTAINER ID   IMAGE           COMMAND       CREATED          STATUS          PORTS     NAMES
e2a06daf01a3   centos:latest   "/bin/bash"   8 seconds ago    Up 8 seconds              centos7
c4690d77c540   ubuntu:latest   "bash"        31 seconds ago   Up 31 seconds             ubuntu
```
4 \
ansible-playbook playbook/site.yml -i playbook/inventory/prod.yml
```
TASK [Print fact] *************************************************************************************************************************************************************
ok: [centos7] => {
    "msg": "el"
}
ok: [ubuntu] => {
    "msg": "deb"
}
```
5 \
Поменял значения переменных \

6 \
ansible-playbook playbook/site.yml -i playbook/inventory/prod.yml
```
TASK [Print fact] *************************************************************************************************************************************************************
ok: [centos7] => {
    "msg": "el default fact"
}
ok: [ubuntu] => {
    "msg": "deb default fact"
}
```
7 \
```
evgeniyfomin@MacBook-Pro-Evgeniy HomeWork8.1 % ansible-vault encrypt playbook/group_vars/deb/examp.yml          
New Vault password: 
Confirm New Vault password: 
Encryption successful
evgeniyfomin@MacBook-Pro-Evgeniy HomeWork8.1 % ansible-vault encrypt playbook/group_vars/el/examp.yml 
New Vault password: 
Confirm New Vault password: 
Encryption successful
```
8 \
ansible-playbook playbook/site.yml -i playbook/inventory/prod.yml --ask-vault-pass
```
TASK [Print fact] *************************************************************************************************************************************************************
ok: [centos7] => {
    "msg": "el default fact"
}
ok: [ubuntu] => {
    "msg": "deb default fact"
}
```
9 \
нужен "local" \
\
10 \
добавил

11 \
```
TASK [Print fact] *************************************************************************************************************************************************************
ok: [localhost] => {
    "msg": "all default fact"
}
ok: [centos7] => {
    "msg": "el default fact"
}
ok: [ubuntu] => {
    "msg": "deb default fact"
}
```