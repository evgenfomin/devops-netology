1.
- Нагрузка СPU, загрузка (место) Накопители (Диски), Загрузка памяти память хоста на котором запущено приложение
- Нагрузка СPU, загрузка (место) Накопители (Диски), Загрузка памяти память хоста на котором запущено БД, если это отдельный хост
- Время запси/чтения диска, покажет доступность дисковой подсистемы
- Доступность страницы приложения, открытие страницы  - с кодом 200, если ПО с WEBUI то проверку осуществлять на удачнотсть авторизации (при отсутсвии штатного Healthcheck)
- Если ПО работает в виде службы - проверку работосопособности служьбы, или альетрнативно проверка запущенного процесса
- Количество открытых соединение с хостом /сервисом
- Проверка доступности БД (connect до БД)
- Проверка времени выполнения запроса если такое доступно, если в БД пишутся данные регулярно с указанием времени записи, то можно проверять время помледей записи/изменения и оценить активность ПО
- Мониторинг БД на предмет долгоработающих блокировок
- Если используются регламеннтые задачи/джобы - проверка их выполнения(успешного завершения) по регламенту
- Проверка Учетных записей на предмет блокировки - работоспособность ТУЗ
- Проверка доступности сетевого соедниение между хоставми работающими в связске с сервисом (приложение и БД в данном случае)
- Нагрузка на сетвой интерфейс.
- Доступность порта до хоста (простые telnet и ping как минимум)
2.
CPU - нагруженность(задержки на комманд процесса) процессора (нагрузка на приложение) \
inodes - загруженность файлово системы (нагрузка ПО на формирование отчетов:кол-во отчетов) \
RAM -  загруженность оперативной памяти \

Предолжу заключить соглашение по дополнительным метрикам (в дополнение можно и SLA к ним)
- Время формирования отчета, можно разбить на несколько метрик : среднее время, а так же минимальное и максимальное время
- Количество ошибок при формировании отчетов, точнее количество отчетов с ошибокй, завершившихся неудачно (не испольненных)
- Доступность приложения в разрезе времени (отклик на работоспособность)

3. 
Все зависит от бюджета \
вариант 1 : Класичесике текстовые логи хранить на сетевом ресурсе (расшарить ресурс) и давать доступ кому необходимо (естественно на чтение) \
Вариант 2 : Использовать систему сбора логов (стэк ELK), предоставить доступ в КИбану для разработчиков на соответсвующие пространства, 
            можно использовать будет в других проектах, и удобнее поиск

4.
 Коды ответов 300-399 - редректы, так же нужно учитывать как успешные, т.к. они не являются по своей сути ошибками, особенно если это в сервисе имеет место быть
Так же коды 100-199 - тинформационные сообщения, которые в свою очередь не являются ошибками.
код 2** - разумно использовать как проверку доступности сервиса, а не едиснтвенный признак работоспособности. \
формула: \
SLI=(summ_2xx_requests+summ_3xx_requests)/summ_all_requests