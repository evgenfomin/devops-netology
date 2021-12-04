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

3\
