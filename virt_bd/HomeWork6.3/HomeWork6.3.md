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
2 \
 Создайте пользователя test в БД c паролем test-pass \
```
mysql> CREATE USER 'test'@'localhost' IDENTIFIED WItH mysql_native_password BY 'test-pass'
    -> ATTRIBUTE '{"fname":"James", "lname":"Pretty"}';
Query OK, 0 rows affected (0.01 sec)

mysql> ALTER USER 'test'@'localhost'
    -> WITH
    -> MAX_QUERIES_PER_HOUR 100
    -> PASSWORD EXPIRE INTERVAL 180 DAY
    -> FAILED_LOGIN_ATTEMPTS 3 PASSWORD_LOCK_TIME 2;
Query OK, 0 rows affected (0.01 sec)
```
Предоставьте привелегии пользователю test на операции SELECT базы test_db \
```
mysql> GRANT SELECT ON test_db.* TO 'test'@'localhost';
Query OK, 0 rows affected, 1 warning (0.02 sec)
```
Используя таблицу INFORMATION_SCHEMA.USER_ATTRIBUTES получите данные по пользователю test \
```
mysql> SELECT * FROM INFORMATION_SCHEMA.USER_ATTRIBUTES WHERE USER='test';
+------+-----------+---------------------------------------+
| USER | HOST      | ATTRIBUTE                             |
+------+-----------+---------------------------------------+
| test | localhost | {"fname": "James", "lname": "Pretty"} |
+------+-----------+---------------------------------------+
1 row in set (0.00 sec)
```
3 \
Исследуйте, какой engine используется в таблице БД test_db и приведите в ответе. \
```
mysql> SHOW CREATE TABLE orders;
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Table  | Create Table                                                                                                                                                                                                                              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| orders | CREATE TABLE `orders` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(80) NOT NULL,
  `price` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
1 row in set (0.00 sec)
```
Измените engine и приведите время выполнения и запрос на изменения из профайлера в ответе: \
```
mysql> ALTER TABLE
TABLE       TABLES      TABLESPACE 
mysql> ALTER TABLE orders ENGINE = MyISAM;
Query OK, 5 rows affected (0.05 sec)
Records: 5  Duplicates: 0  Warnings: 0

mysql> ALTER TABLE orders ENGINE = InnoDB;
Query OK, 5 rows affected (0.06 sec)
Records: 5  Duplicates: 0  Warnings: 0
```
```
mysql> SHOW PROFILES;
+----------+------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Query_ID | Duration   | Query                                                                                                                                                                                |
+----------+------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|       14 | 0.05163525 | ALTER TABLE orders ENGINE = MyISAM                                                                                                                                                   |
|       15 | 0.05948800 | ALTER TABLE orders ENGINE = InnoDB                                                                                                                                                   |
+----------+------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
15 rows in set, 1 warning (0.00 sec)
```
4 \
Скорость IO важнее сохранности данных \
innodb_flush_log_at_trx_commit = 0 
  - 0 - самый производительный, но небезопасный вариант
  - 1 - сохранность данных — это приоритет номер один
  - 2 - когда небольшая потеря данных не критична 
  
Нужна компрессия таблиц для экономии места на диске \
innodb_file_format=Barracuda \
Размер буффера с незакомиченными транзакциями 1 Мб \
innodb_log_buffer_size =1M \
Буффер кеширования 30% от ОЗУ \
innodb_buffer_pool_size = 640M \
Размер файла логов операций 100 Мб \
innodb_log_file_size = 100M

Пример моего файла my.cnf (без закоментированных строк):
```
[mysqld]
pid-file        = /var/run/mysqld/mysqld.pid
socket          = /var/run/mysqld/mysqld.sock
datadir         = /var/lib/mysql
secure-file-priv= NULL

innodb_flush_log_at_trx_commit = 0
innodb_file_format=Barracuda
innodb_log_buffer_size =1M
innodb_buffer_pool_size = 640M
innodb_log_file_size = 100M

!includedir /etc/mysql/conf.d/
```