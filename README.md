# Проект postgres-вакансии

## Описание пректа

Проект представляет собой набор команд для получения и фильрации вакансий с сервиса hh.ru через базу данных
Запросы отправляются через api с помощью библиотеки requests.
Хранение осуществляется в базе данных hhrujobs.
Взаимодействие с базой данных выполнено через библиотеку psycopg2.

## Подготовка

### Настройка poetry

В проекте используется пакетный менеджер poetry. Для его настройки необходимо выпольнить следующие шаги:
- установить poetry командой pip install poetry
- создать и активировать виртуальное окружение командой poetry shell
- установить зависимости командой poetry install

### Настройка базы данных
Для работы с проектом используется субд postgresql.
Чтобы начать использовать команды в проекте, необходимо;
- ввести в терминал postgre набор команд, описанных в файле sql.
- Сохранить свой пароль от postgre в системных переменных средах как PASSWD

## Краткий экскурс

Работа приложения описана в файле postgres_proj/main.py

## Команды для пользвоания

Для использования приложения написаны несклько скриптов:
- load-vacancies: загружает n вакансий по ключевым словам
- get-companies-and-vacancies-count: возвращает количество работодателей и вакансий
- get-all-vacancies: возвращает все вакансии в формате Работодатель, название вакансии, зарплата, ссылка
- get-avg-salary: возвразает среднюю зарплату
- get-vacancies-with-higher-salary: возвращает вакансии, с зарплатой выше средней в формате Работодатель, название вакансии, зарплата, ссылка
- get-vacancies-with-keyword: возвращает вакансии, в названии или требовании которых присутсвуют заданные ключевые слова

### Для использования скриптов необходимо использовать команду:

- poetry run название-скрипта

