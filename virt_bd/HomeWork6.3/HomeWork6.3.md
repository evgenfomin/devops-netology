1 \
Запускаем docker:
```
docker run --rm --name mysql -e MYSQL_ROOT_PASSWORD=qaz -v /home/evgeniy/tmp/mysql_data:/var/lib/mysql -d -p "3306:3306" mysql:8.0
```
Восстанавливаем БД из backup
```
mysql -p test_db < test_dump.sql
```
Найдите команду для выдачи статуса БД и приведите в ответе из ее вывода версию сервера БД
```
mysql> \s
--------------
mysql  Ver 8.0.27 for Linux on x86_64 (MySQL Community Server - GPL)

Connection id:		15
Current database:	
Current user:		root@localhost
SSL:			Not in use
Current pager:		stdout
Using outfile:		''
Using delimiter:	;
Server version:		8.0.27 MySQL Community Server - GPL
Protocol version:	10
Connection:		Localhost via UNIX socket
Server characterset:	utf8mb4
Db     characterset:	utf8mb4
Client characterset:	latin1
Conn.  characterset:	latin1
UNIX socket:		/var/run/mysqld/mysqld.sock
Binary data as:		Hexadecimal
Uptime:			16 min 52 sec

Threads: 2  Questions: 53  Slow queries: 0  Opens: 138  Flush tables: 3  Open tables: 56  Queries per second avg: 0.052
--------------
```
Подключаемся к БД 
```
mysql> use test_db
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
```
Выводим таблицы:
```
mysql> SHOW TABLES;
+-------------------+
| Tables_in_test_db |
+-------------------+
| orders            |
+-------------------+
1 row in set (0.00 sec)

```
Выводим количество строк с ценой больше 300:
```
mysql> SELECT COUNT(*) FROM orders WHERE price > 300;
+----------+
| COUNT(*) |
+----------+
|        1 |
+----------+
1 row in set (0.00 sec)
```
