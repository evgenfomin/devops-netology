1\
https://hub.docker.com/repository/docker/29072014/my_nginx

2\
Высоконагруженное монолитное java веб-приложение;
 - физический сервер, т.к. монолитное, селдовательно без изменения кода 
   и так как высоконагруженное, то необходим физический доступ к ресурсами

Nodejs веб-приложение;
 - это веб приложение значит докер

Мобильное приложение c версиями для Android и iOS;
 - Виртаулка т.к приложение в докере не имеет GUI

Шина данных на базе Apache Kafka;
 - я думаю можно и виртуалку и контейнер,если потеря данных при потере контенйера не является критичной то можно и в контейнере.

Elastic stack для реализации логирования продуктивного веб-приложения - три ноды elasticsearch, два logstash и две ноды kibana;
 - сам elasticsearch лучше на виртуалку, отказоустойчивость решается на уровне кластера, 
   kibana и logstash можно вынести в докер контейнер, или так же на виртуалках.
   существуют решения и в таком и в таком исполнении

Мониторинг-стек на базе prometheus и grafana;
 - сами системы не хранят как таковых данны, можно развернуть на docker

Mongodb, как основное хранилище данных для java-приложения;
 - можно использовать Виртуальную машину, т.к. хранилище и  не сказано что высоконагруженное
   в Контейнере хранить БД с данными не подходит

Gitlab сервер для реализации CI/CD процессов и приватный (закрытый) Docker Registry:
 - физический сервер, т.к необходимо много места для хранения данных

3\
centos: \
[root@5b8dafe5f32f data]# touch 1.txt \
[root@5b8dafe5f32f data]# echo "test" > 1.txt \ 
[root@5b8dafe5f32f data]# ls -la \
total 12 \
drwxrwxr-x 2 1000 1000 4096 Nov  8 07:18 . \
drwxr-xr-x 1 root root 4096 Nov  8 07:13 .. \ 
-rw-r--r-- 1 root root    5 Nov  8 07:18 1.txt \

host: \
vagrant@server1:~/data$ touch 2.txt \
vagrant@server1:~/data$ ls -la \
total 12 \
drwxrwxr-x 2 vagrant vagrant 4096 Nov  8 07:19 . \
drwxr-xr-x 9 vagrant vagrant 4096 Nov  8 06:51 .. \
-rw-r--r-- 1 root    root       5 Nov  8 07:18 1.txt \ 
-rw-rw-r-- 1 vagrant vagrant    0 Nov  8 07:19 2.txt \

debian: \
root@f4022f693275:/data# ls -la \
total 12 \
drwxrwxr-x 2 1000 1000 4096 Nov  8 07:19 . \
drwxr-xr-x 1 root root 4096 Nov  8 07:08 .. \
-rw-r--r-- 1 root root    5 Nov  8 07:18 1.txt \
-rw-rw-r-- 1 1000 1000    0 Nov  8 07:19 2.txt \


