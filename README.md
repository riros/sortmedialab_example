SoftMediaLab
============


Задание
------------------

Реализовать REST АПИ для клиентского приложения, которое должно отображать страницу со списком студентов с возможностями:

1) добавить нового студента в этот список;
2) удалить существующего студента;
3) отредактировать существующего студента;

У студента есть поля:
- ФИО
- дата рождения
- успеваемость (опционально из справочника неуд/уд/хор/отл)

Предпочтительные технологии:

* python
* django
* swagger

Инструкции для запуска
-----------------------

####  для разработчика
1) установка и активация окружения <pre> virtualenv ../venv && source ../venv/bin/activate</pre>

2) установка пакетов <pre>pip install -r requirements.txt</pre>

3) инициализация базы <pre>make init_db</pre>

4) запуск сервера для разработки <pre>make serve</pre>

##### Пути приложения
<pre>/ - апи сервиса
/docs - swagger
/docs/redoc - REDoc
/admin - админка Django</pre>

####  для запуска на сервере

<pre>make prod_serve</pre>

#### Заметки

* У приложения в моделях использованы uuid в качестве идентификаторов, это
позволяет избежать проблем при загрузке фикстур и слиянии баз.
Отсутствует конфликт счетчиков индексов в бд.

* файл пакетов разбит на 2 составляющие, в dev.requirements.txt хранятся пакеты без версий, чтобы при разработке иметь
последние актуальные, за исключением явно указанных из за багов. А в requirements.txt хранятся последние зафиксированные
 версии, которые проверены
 разработчиком. для их фиксации нужно запустить <pre> make freeze </pre>

