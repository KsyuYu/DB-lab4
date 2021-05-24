# Лабораторна робота №1 студентки групи КМ-81 Юр'єваї Ксенії

Перед запуском програми додайте в папку проекту файли *Odata2019File.csv*, *Odata2020File.csv*

## Інструкція по запуску
Встановити MongoDB та запустити його:
В окремому терміналі/консолі запустити

- `"C:\Program Files\MongoDB\Server\4.4\bin\mongod.exe" --dbpath="C:\Program Files\MongoDB\Server\4.4\data"`

Послідовно виконати наступні команди:

- Linux/MacOS

```
python3 -m pip install virtualenv
python3 -m venv bd_env
source bd_env/bin/activate
python3 -m pip install -r requirements.dev
python3 main.py
```

- Windows

```
py -m pip install --user virtualenv
py -m venv bd_env
.\bd_env\Scripts\activate
py -m pip install -r requirements.dev
py main.py
```

## Результати роботи програми

#### Приклад файлу LastRow.txt

2020, 379290

#### Приклад файлу database_logs.log

Протягом роботи програма записує свої дії у файл database_logs.log.  
На початку і в кінці додавання даних фіксується час поточної ітерації. Наприклад, `Work time 0:00:38.678979`

Приклад логів:

```
2021-03-07 18:51:00,066: Creating table
2021-03-07 18:51:00,137: GeneralTable has created
2021-03-07 18:51:00,144: Inserting data from 0 row from Odata2019File.csv
2021-03-07 19:11:05,196: Inserting data from 0 row from Odata2020File.csv
2021-03-07 19:32:51,335: Finish inserting at 2021-03-07 19:32:51.334136
2021-03-07 19:32:51,335: Work time 0:41:51.189724
2021-03-07 19:32:51,335: Getting data for query
2021-03-07 19:32:53,149: Query data has recorded into query.csv
2021-03-07 19:32:53,151: The end
2021-05-23 22:06:02,114: Start time 2021-05-23 22:06:02.114615
2021-05-23 22:06:02,119: Create collections
2021-05-23 22:06:33,538: Start time 2021-05-23 22:06:33.538768
2021-05-23 22:06:33,549: Create collections
2021-05-23 22:06:33,564: Inserting data from 0 row from file for 2019 year
2021-05-23 22:07:24,643: Start time 2021-05-23 22:07:24.643333
2021-05-23 22:07:24,646: Create collections
2021-05-23 22:07:24,660: Inserting data from 0 row from file for 2019 year
2021-05-23 22:08:14,803: Break time 2021-05-23 22:08:14.803811
2021-05-23 22:08:14,804: Executing time 0:00:50.160478
2021-05-23 22:08:14,804: Fallen: localhost:27017: [WinError 10054] An existing connection was forcibly closed by the remote host
2021-05-23 22:12:49,721: Start time 2021-05-23 22:12:49.721437
2021-05-23 22:12:49,724: Create collections
2021-05-23 22:12:49,759: Inserting data from 0 row from file for 2019 year
2021-05-23 22:14:24,793: Break time 2021-05-23 22:14:24.793304
2021-05-23 22:14:24,793: Executing time 0:01:35.071867
2021-05-23 22:14:24,793: Fallen: localhost:27017: [WinError 10054] An existing connection was forcibly closed by the remote host
2021-05-23 22:23:06,933: Start time 2021-05-23 22:23:06.933127
2021-05-23 22:23:06,940: Inserting data from 0 row from file for 2019 year
2021-05-23 22:24:46,937: Break time 2021-05-23 22:24:46.937198
2021-05-23 22:24:46,937: Executing time 0:01:40.004071
2021-05-23 22:24:46,937: Fallen: localhost:27017: [WinError 10054] An existing connection was forcibly closed by the remote host
2021-05-23 22:26:19,419: Start time 2021-05-23 22:26:19.419102
2021-05-23 22:26:19,425: Inserting data from 115810 row from file for 2019 year
2021-05-23 22:29:40,441: Inserting from Odata2019File.csv is finished
2021-05-23 22:29:40,441: Inserting data from 0 row from file for 2020 year
2021-05-23 22:31:00,689: Break time 2021-05-23 22:31:00.689989
2021-05-23 22:31:00,690: Executing time 0:04:41.270887
2021-05-23 22:31:00,690: Fallen: localhost:27017: [WinError 10054] An existing connection was forcibly closed by the remote host
2021-05-23 22:31:27,919: Start time 2021-05-23 22:31:27.919273
2021-05-23 22:31:27,939: Inserting data from 55620 row from file for 2020 year
2021-05-23 22:36:21,306: Break time 2021-05-23 22:36:21.306852
2021-05-23 22:36:21,306: Executing time 0:04:53.387579
2021-05-23 22:36:21,306: Fallen: localhost:27017: [WinError 10054] An existing connection was forcibly closed by the remote host
2021-05-23 22:36:49,112: Start time 2021-05-23 22:36:49.112179
2021-05-23 22:36:49,120: Inserting data from 338400 row from file for 2020 year
2021-05-23 22:37:53,495: Inserting from Odata2020File.csv is finished
2021-05-23 22:37:53,495: End time 2021-05-23 22:37:53.495617
2021-05-23 22:37:53,495: Inserting executing time 0:01:04.383438
2021-05-23 22:37:53,495: Getting data for query
2021-05-23 22:39:14,929: Start time 2021-05-23 22:39:14.929309
2021-05-23 22:39:14,934: Getting data for query
2021-05-23 22:39:29,420: Users query data recorded into query.csv
2021-05-23 22:39:29,423: Program is finished
```

#### Файл query.csv

Отриманий файл є результатом роботи програми. Згідно із завданням `Варіант 5. Порівняти середній бал з Історії України у кожному регіоні у 2020 та 2019 роках серед тих кому було зараховано тест` у файлі наведені відомості про регіон, рік проведення ЗНО та середній бал з історії.