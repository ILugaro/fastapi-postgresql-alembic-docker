# FastAPI + SQLAlchemy + Alembic + Paydantic

Тестовое задание на Python backend разработчик

## Задание

Используя SQLAlchemy и alembic создать базу данных postgreSQL по xlsx файлу (в папке Files). 
С помощью FastAPI сделать роутер для получения этих данных.
Создать докер файл для запуска микросервиса.


## Запросы

Получить всю продукцию: [http://127.0.0.1:8004/api/product/all_products](http://127.0.0.1:8004/api/product/all_products)

Получить продукт по внутреннему id [http://127.0.0.1:8004/api/product/product/](http://127.0.0.1:8004/api/product/product/)