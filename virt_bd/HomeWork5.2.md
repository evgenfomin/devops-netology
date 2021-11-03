1 \

CI - Continuous Integration, сборка например все веток в одно рабочую \
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
Спасибо за обратную связь \
vagrant@server1:~$ docker ps \
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES