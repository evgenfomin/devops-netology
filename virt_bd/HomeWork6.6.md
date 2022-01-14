1 \
напишите список операций, которые вы будете производить для остановки запроса пользователя \
db.currentOp() - для определения текущей операции \
db.killOp(<opId>) - для прерывания опереции по ID

что бы избежать такого можно в запросе указать maxTimeMS()

2 \
При масштабировании сервиса до N реплик вы увидели, что:
 - сначала рост отношения записанных значений к истекшим
 - Redis блокирует операции записи

Как вы думаете, в чем может быть проблема?

необходимо включить монитор задержки и понять где сервер блокирует \
также задержки могут быть из за:
 - выполняются медленные команды которые блокируют сервер
 - для пользователей ЕС2 используются устаревшие ЕС2 инстансы
 - в ядре не отключены Transparent huge pages это можно сделать 
   - echo never > /sys/kernel/mm/transparent_hugepage/enabled

3 \
Вы подняли базу данных MySQL для использования в гис-системе. При росте количества записей, в таблицах базы, пользователи начали жаловаться на ошибки вида:

InterfaceError: (InterfaceError) 2013: Lost connection to MySQL server during query u'SELECT..... ' \
Как вы думаете, почему это начало происходить и как локализовать проблему?

Какие пути решения данной проблемы вы можете предложить?

Скорей всего это происходит из за того что данные не успевает завершиться передача данных \
необходимо увеличить значение connect_timeout, interactive_timeout, wait_timeout net_read_timeout \

4 \
После запуска пользователи начали жаловаться, что СУБД время от времени становится недоступной. В dmesg вы видите, что:
postmaster invoked oom-killer \
это значит, что не хватает памяти и ос завершает процессы утилизирующие \
память, чтобы этого не проиходило необходимо увеличеть память или выставить \
ограничение в настройках PG на использование ресурсов хоста\ 
Мои действия были бы увеличил бы память