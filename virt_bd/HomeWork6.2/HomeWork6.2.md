1
```
version: "3.9"
services:
  postgres:
    image: "postgres:12.9"
    container_name: "postgres"
    environment:
      POSTGRES_PASSWORD: "pgpwd4habr"
      PGDATA: "/var/lib/postgresql/data/pgdata"
    volumes:
      - "/home/evgeniy/test/sql/data:/var/lib/postgresql/data/pgdata"
      - "/home/evgeniy/test/sql/backup:/var/lib/postgresql/data"
    ports:
      - "5432:5432"
```
2
Создаем БД
```
postgres=# CREATE DATABASE test_db;
CREATE DATABASE
```
Создаем пользователя
```
postgres=# CREATE ROLE "test-admin-user" SUPERUSER CREATEDB CREATEROLE INHERIT LOGIN;
CREATE ROLE
```
Создаем таблицу oders
```
test_db=# CREATE TABLE orders (id integer PRIMARY KEY, name text, price integer);
CREATE TABLE
test_db=# \dt
             List of relations
 Schema |  Name  | Type  |      Owner      
--------+--------+-------+-----------------
 public | orders | table | test-admin-user
(1 row)
```
Создаем таблицу clients
```
test_db=# CREATE TABLE clients (id integer PRIMARY KEY, lastname text, country text, booking integer, FOREIGN KEY (booking) REFERENCES orders (id));
CREATE TABLE
test_db=# \dt
             List of relations
 Schema |  Name   | Type  |      Owner      
--------+---------+-------+-----------------
 public | clients | table | test-admin-user
 public | orders  | table | test-admin-user
(2 rows)
```
Создаем пользователя test-simple-user и выдаем права на test_db
```
test_db=# CREATE ROLE "test-simple-user" NOSUPERUSER NOCREATEDB NOCREATEROLE NOINHERIT LOGIN;
CREATE ROLE
test_db=# GRANT SELECT ON ALL TABLES IN SCHEMA public TO "test-simple-user";
GRANT
test_db=# GRANT INSERT ON ALL TABLES IN SCHEMA public to "test-simple-user";
GRANT
test_db=# GRANT UPDATE ON ALL TABLES IN SCHEMA public TO "test-simple-user";
GRANT
test_db=# GRANT DELETE ON ALL TABLES IN SCHEMA public TO "test-simple-user"
GRANT
```
\
Итоговый список БД \
![итоговый список баз данных](https://github.com/evgenfomin/devops-netology/blob/main/virt_bd/HomeWork6.2/Screenshot%20from%202021-12-04%2013-42-10.png) \
Описание таблицы orders: \
![orders](https://github.com/evgenfomin/devops-netology/blob/main/virt_bd/HomeWork6.2/Screenshot%20from%202021-12-04%2015-56-06.png) \
Описание таблицы clients: \
![clients](https://github.com/evgenfomin/devops-netology/blob/main/virt_bd/HomeWork6.2/Screenshot%20from%202021-12-04%2015-58-59.png) \
SQL запрос и сама таблица с правами нат таблицами \
![sql_order](https://github.com/evgenfomin/devops-netology/blob/main/virt_bd/HomeWork6.2/Screenshot%20from%202021-12-04%2016-06-14.png) \

3 \
```
test_db=# INSERT INTO orders VALUES (1, 'Шоколад', 10), (2, 'Принтер', 3000), (3, 'Книга', 500), (4, 'Монитор', 7000), (5, 'Гитара', 4000);
INSERT 0 5
test_db=# INSERT INTO clients VALUES (1, 'Иванов Иван Иванович', 'USA'), (2, 'Петров Петр Петрович', 'Canada'), (3, 'Иоган Себастьян Бах', 'Japan');
INSERT 0 3
test_db=# INSERT INTO clients VALUES (4, 'Ронни Джеймс Дио', 'Russia'), (5, 'Ritchie Blackmore', 'Russia');
INSERT 0 2
test_db=# SELECT COUNT (*) FROM orders;
 count 
-------
     5
(1 row)

test_db=# SELECT COUNT (*) FROM clients;
 count 
-------
     5
(1 row)
```
4 \
```
test_db=# UPDATE clients set booking=3 where id=1;
UPDATE 1
test_db=# UPDATE clients set booking=4 where id=2;
UPDATE 1
test_db=# UPDATE clients set booking=5 where id=3;
test_db=# SELECT * FROM clients where booking is not null
test_db-# ;
 id |       lastname       | country | booking 
----+----------------------+---------+---------
  1 | Иванов Иван Иванович | USA     |       3
  2 | Петров Петр Петрович | Canada  |       4
  3 | Иоган Себастьян Бах  | Japan   |       5
(3 rows)
```
5 \
```
test_db=# EXPLAIN SELECT * FROM clients where booking is not null;
                        QUERY PLAN                         
-----------------------------------------------------------
 Seq Scan on clients  (cost=0.00..18.10 rows=806 width=72)
   Filter: (booking IS NOT NULL)
(2 rows)

test_db=# 
```
Показывает стоимость(нагрузку на исполнение) запроса , и фильтрацию по полю Booking для выборки.

6 \
Команда для создания dump: \
pg_dump -U postgres -W test_db > /var/lib/postgresql/data/backup_test_db\
Восстановление: \n
psql -U postgres test_db < /var/lib/postgresql/data/backup_test_db \n
```
test_db=# SELECT * FROM orders;
 id |  name   | price 
----+---------+-------
  1 | Шоколад |    10
  2 | Принтер |  3000
  3 | Книга   |   500
  4 | Монитор |  7000
  5 | Гитара  |  4000
(5 rows)

test_db=# SELECT * FROM clients;
 id |       lastname       | country | booking 
----+----------------------+---------+---------
  4 | Ронни Джеймс Дио     | Russia  |        
  5 | Ritchie Blackmore    | Russia  |        
  1 | Иванов Иван Иванович | USA     |       3
  2 | Петров Петр Петрович | Canada  |       4
  3 | Иоган Себастьян Бах  | Japan   |       5
(5 rows)

test_db=# 

```