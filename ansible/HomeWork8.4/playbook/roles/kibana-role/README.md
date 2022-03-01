Elascticsearch role
=========

Роль для установки filebeat на хостах с ОС:CentOS.

Requirements
------------

Поддерживаются только ОС семейств CentOS.

Role Variables
--------------

| Variable name  | Default | Description                                                       |
|----------------|----------|-------------------------------------------------------------------|
| kibana_version | "7.14.0" | Параметр, который определяет какой версии kibana будет установлен |

Example Playbook
----------------

    - hosts: all
      roles:
         - { role: mnt-homeworks-ansible }

License
-------

BSD

Author Information
------------------
Evgeniy Fomin