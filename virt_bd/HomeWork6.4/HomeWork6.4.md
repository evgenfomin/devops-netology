1 \

 - вывода списка БД: \l[+]   [PATTERN]      list databases
 - подключения к БД: \c[onnect] {[DBNAME|- USER|- HOST|- PORT|-] | conninfo}
 - подключения к БД: \dt[S+] [PATTERN]      list tables
 - вывода описания содержимого таблиц: \ds[S+] [PATTERN]      list sequences
 - выхода из psql: \q                     quit psql

\
2 \
```postgres=# CREATE DATABASE test_database;
CREATE DATABASE
postgres=# \l
                                   List of databases
     Name      |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges   
---------------+----------+----------+------------+------------+-----------------------
 postgres      | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0     | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
               |          |          |            |            | postgres=CTc/postgres
 template1     | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
               |          |          |            |            | postgres=CTc/postgres
 test_database | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
(4 rows)
```

Подключитесь к восстановленной БД и проведите операцию ANALYZE для сбора статистики по таблице \
```
test_database=# ANALYZE VERBOSE public.orders;
INFO:  analyzing "public.orders"
INFO:  "orders": scanned 1 of 1 pages, containing 8 live rows and 0 dead rows; 8 rows in sample, 8 estimated total rows
ANALYZE
```
Используя таблицу pg_stats, найдите столбец таблицы orders с наибольшим средним значением размера элементов в байтах \
```
test_database=# select avg_width from pg_stats where tablename='orders';
 avg_width 
-----------
         4
        16
         4
(3 rows)
```
3 \
Как я понял данный метод называется Декларативное секционирование. \
Для начала скопируем нашу таблицу: 
```
test_database=# alter table orders rename to orders_copy;
ALTER TABLE
```
Пересоздадим таблицу orders, но как секционированную таблицу с указанием метода разбиения:
```
test_database=# create table orders (id integer, title varchar(80), price integer) partition by range (price);
CREATE TABLE
```
Создаем секции и указываем границы:
```
test_database=# create table orders_less_500 partition of orders for values from (0) to (500);
CREATE TABLE
test_database=# create table orders_more_500 partition of orders for values from (500) to (999999999);
CREATE TABLE
```
Заполняем нашу таблицу данными:
```
test_database=# insert into orders (id, title, price) select * from orders_copy;
INSERT 0 8
```
Сморим наши таблицы:
```
test_database=# \dt
                    List of relations
 Schema |      Name       |       Type        |  Owner   
--------+-----------------+-------------------+----------
 public | orders          | partitioned table | postgres
 public | orders_copy     | table             | postgres
 public | orders_less_500 | table             | postgres
 public | orders_more_500 | table             | postgres
(4 rows)

test_database=# select * from orders_less_500;
 id |        title         | price 
----+----------------------+-------
  1 | War and peace        |   100
  3 | Adventure psql time  |   300
  4 | Server gravity falls |   300
  5 | Log gossips          |   123
  7 | Me and my bash-pet   |   499
(5 rows)

test_database=# select * from orders_more_500;
 id |       title        | price 
----+--------------------+-------
  2 | My little database |   500
  6 | WAL never lies     |   900
  8 | Dbiezdmin          |   501
(3 rows)
```

4 \
Создаем backup БД: \
pg_dump -U postgres test_database > /var/lib/postgresql/data/pgdata/backup_test_database \
Для уникальности можно добавить индекс или первичный ключ.