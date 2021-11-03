1 \

CL - Continuous Integration, сборка например все веток в одно рабочую \
CD - Continuous Delivery, доставка новой версии на тестовый стенд напрмер и тестирование \
CD - Continuous Deployment, деплой на боевом сервере \
самым основным я считаю 2 паттерн, на котором происходит либо откат либо уже запуск в продакшн \

2 \
   
 для управления удаленным хостом неоюходимо иметь тоолько ssh доступ, так же достаточно легкий вход в плане знаний
вся конфигурация описывается на python при помощи языка разметки yaml

3 \
   
 evgeniy@evgeniy-PR:~$ ansible --version \
    ansible 2.9.6 \
   evgeniy@evgeniy-PR:~$ vagrant --version \
    Vagrant 2.2.6 \
    evgeniy@evgeniy-PR:~$ vboxmanage --version \
    6.1.26_Ubuntur145957

4 \

Запускается ВМ но на этапе ansible вылетает ошибка: \

==> server1.netology: Running provisioner: ansible...
Vagrant has automatically selected the compatibility mode '2.0'
according to the Ansible version installed (2.9.6).

Alternatively, the compatibility mode can be specified in your Vagrantfile:
https://www.vagrantup.com/docs/provisioning/ansible_common.html#compatibility_mode

    server1.netology: Running ansible-playbook...
ERROR! Syntax Error while loading YAML.
  mapping values are not allowed in this context

The error appears to be in '/home/evgeniy/vms/vms_test/ansible/provision.yml': line 4, column 11, but may
be elsewhere in the file depending on the exact syntax problem.

The offending line appears to be:

  — hosts: nodes
    become: yes
          ^ here
Ansible failed to complete successfully. Any error output should be
visible above. Please fix these errors and try again.
\

Файл provision.yml добавил в репо, все изрыл не пойму в чем дело нет там синтатической ошибки не какой, \ 
помогите разобраться

