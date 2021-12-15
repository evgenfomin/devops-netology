1 \
Dockerfile: \
```
FROM centos:7

ENV PATH=/usr/lib:$PATH

RUN rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch
RUN echo "[elasticsearch]" >> /etc/yum.repos.d/elasticsearch.repo &&\
    echo "name=Elasticsearch repository for 7.x packages" >> /etc/yum.repos.d/elasticsearch.repo &&\
    echo "baseurl=https://artifacts.elastic.co/packages/7.x/yum" >> /etc/yum.repos.d/elasticsearch.repo &&\
    echo "gpgcheck=1" >> /etc/yum.repos.d/elasticsearch.repo &&\
    echo "gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch" >> /etc/yum.repos.d/elasticsearch.repo &&\
    echo "enabled=0" >> /etc/yum.repos.d/elasticsearch.repo &&\
    echo "autorefresh=1" >> /etc/yum.repos.d/elasticsearch.repo &&\
    echo "type=rpm-md" >> /etc/yum.repos.d/elasticsearch.repo
RUN yum install --enablerepo=elasticsearch elasticsearch -y
COPY elasticsearch.yml /etc/elasticsearch/

RUN mkdir /usr/share/elasticsearch/snapshots &&\
    chown elasticsearch:elasticsearch /usr/share/elasticsearch/snapshots
RUN mkdir /var/lib/logs \
    && chown elasticsearch:elasticsearch /var/lib/logs \
    && mkdir /var/lib/data \
    && chown elasticsearch:elasticsearch /var/lib/data
USER elasticsearch
CMD ["/usr/sbin/init"]
CMD ["/usr/share/elasticsearch/bin/elasticsearch"]
```
ответ по запросу:
```
{
  "name" : "4fcbaf072d8b",
  "cluster_name" : "netology_test",
  "cluster_uuid" : "1dVOReJKSkO4GAbtYaXj9Q",
  "version" : {
    "number" : "7.16.1",
    "build_flavor" : "default",
    "build_type" : "rpm",
    "build_hash" : "5b38441b16b1ebb16a27c107a4c3865776e20c53",
    "build_date" : "2021-12-11T00:29:38.865893768Z",
    "build_snapshot" : false,
    "lucene_version" : "8.10.1",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
```
\
2 \
добавьте в elasticsearch 3 индекса, в соответствии со таблицей
```
curl -X PUT localhost:9200/ind-1 -H 'Content-Type: application/json' -d'{ "settings": { "number_of_shards": 1,  "number_of_replicas": 0 }}'
{"acknowledged":true,"shards_acknowledged":true,"index":"ind-1"}
```
Получите список индексов и их статусов, используя API и приведите в ответе на задание
```
evgeniy@evgeniyPR:~$ curl http://localhost:9200/_cat/indices
green  open .geoip_databases ve8uT1VNQeSogJd16K5t_g 1 0 42 0 41.2mb 41.2mb
green  open ind-1            cHuGjRVOSnOe-_EZD2iTNA 1 0  0 0   226b   226b
yellow open ind-3            ZuWlkiZ1RBCEIL5QJX7Bvw 4 2  0 0   904b   904b
yellow open ind-2            8oRNf5JATdetnFfaRqPIDw 2 1  0 0   452b   452b
```
Получите состояние кластера elasticsearch, используя API
```
vgeniy@evgeniyPR:~$ curl http://localhost:9200/_cluster/health?pretty
{
  "cluster_name" : "netology_test",
  "status" : "yellow",
  "timed_out" : false,
  "number_of_nodes" : 1,
  "number_of_data_nodes" : 1,
  "active_primary_shards" : 10,
  "active_shards" : 10,
  "relocating_shards" : 0,
  "initializing_shards" : 0,
  "unassigned_shards" : 10,
  "delayed_unassigned_shards" : 0,
  "number_of_pending_tasks" : 0,
  "number_of_in_flight_fetch" : 0,
  "task_max_waiting_in_queue_millis" : 0,
  "active_shards_percent_as_number" : 50.0
}
```
Часть индексов желтые потому что указанно количество реплик, но на самом деле их нет т.к одна нода \
Удалите все индексы:
```
evgeniy@evgeniyPR:~$ curl -XDELETE localhost:9200/ind-1?pretty
{
  "acknowledged" : true
}
evgeniy@evgeniyPR:~$ curl -XDELETE localhost:9200/ind-2?pretty
{
  "acknowledged" : true
}
evgeniy@evgeniyPR:~$ curl -XDELETE localhost:9200/ind-3?pretty
{
  "acknowledged" : true
}
```

3 \
