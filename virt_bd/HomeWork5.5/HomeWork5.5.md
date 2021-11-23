1\
replication - сервис запускается только на тех нодах на которых мы задаем \
global - сервис запускается на всех нодах \
\
лидер задается вручную командой docker swarm init, если данная нода упала то лидером может  \
стать любая из управляющих нод \
\
Overlay-сеть создает подсеть, которую могут использовать контейнеры в разных хостах swarm-кластера.\
Контейнеры на разных физических хостах могут обмениваться данными по overlay-сети \
(если все они прикреплены к одной сети).

2 \
все получилось \
![alt docker node ls](https://github.com/evgenfomin/devops-netology/blob/main/virt_bd/HomeWork5.5/Screenshot%20from%202021-11-23%2010-26-01.png) \
\
3 \
![alt docker service ls](https://github.com/evgenfomin/devops-netology/blob/main/virt_bd/HomeWork5.5/Screenshot%20from%202021-11-23%2010-28-00.png) \
\
4 \
Vожно добавить дополнительную уровень безопасности создав ключи \
Если докер уже запушен, то как раз командой docker swarm update --autolock=true \
мы активируем даную функцию \
![alt docker swarm update](https://github.com/evgenfomin/devops-netology/blob/main/virt_bd/HomeWork5.5/Screenshot%20from%202021-11-23%2010-51-40.png) \
