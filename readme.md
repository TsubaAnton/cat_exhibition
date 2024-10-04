REST API онлайн выставка котят

Технические требования
Python 3.9+
Django 3+
DRF 3.10+
PostgreSQL 10+

Перед запуском web-приложения необходимо:
1. Создать базу данных.
2. Создать и применить миграции.
3. Установить все необходимые пакеты из requirements.txt
4. Заполнить файл .env

Используйте команду 'python manage.py csu' для создания суперпользователя.

Документация доступна по следующему адресу: http://localhost:8000/swagger/

Для запуска тестов используйте команду 'pytest'.

Для запуска приложения через Docker используйте следующие команды:
1. docker-compose build
2. docker-compose up
