"""Данные для заполнения тестовой БД"""
from datetime import datetime

from app import Category, CategoryPath, City, Nomenclature, Product

# формировани наполнения для таблиц категорий и городов, которое происходит при парсинге excel
category_bases: dict[str, Category] = {'igrushki_i_igry': Category(category='igrushki_i_igry')}
category_path_bases: dict[str, CategoryPath] = {
    'Главная::Детские игрушки::Детские конструкторы::Блочные конструкторы::Блочные SLUBAN': CategoryPath(
        category_path='Главная::Детские игрушки::Детские конструкторы::Блочные конструкторы::Блочные SLUBAN'
    ),
    'Главная::Детские игрушки::Детские конструкторы::Блочные конструкторы::Блочные LEGO': CategoryPath(
        category_path='Главная::Детские игрушки::Детские конструкторы::Блочные конструкторы::Блочные LEGO'
    ),
    'Главная::Детские игрушки::Настольные игры::Развивающие::Развивающие Djeco': CategoryPath(
        category_path='Главная::Детские игрушки::Настольные игры::Развивающие::Развивающие Djeco'
    ),
}
city_bases: dict[str, City] = {'msk': City(city='msk')}
nomenclature_bases: dict[str, Nomenclature] = {
    'Блочные конструкторы': Nomenclature(nomenclature='Блочные конструкторы'),
    'Развивающие': Nomenclature(nomenclature='Развивающие'),
}

# формировани наполнения для таблицы продуктов
products: list[Product] = [
    Product(
        name='Конструктор SLUBAN Сапфировый замок',
        articul='M38-B0610',
        gost='ТУ 17.23.13-004',
        brand='LEGO',
        category=category_bases['igrushki_i_igry'],
        nomenclature=nomenclature_bases['Блочные конструкторы'],
        category_path=category_path_bases[
            'Главная::Детские игрушки::Детские конструкторы::Блочные конструкторы::Блочные SLUBAN'
        ],
        price=4599,
        url_id='2867791',
        warehouse='Lego & co',
        count=16,
        instock='ожидается',
        city=city_bases['msk'],
        updated_at=datetime(2024, 1, 28, 23, 49),
        discount_price=2719,
        razmer='19х19х25',
    ),
    Product(
        name='M38-B0610',
        articul='76409',
        gost=None,
        brand='-',
        category=category_bases['igrushki_i_igry'],
        nomenclature=nomenclature_bases['Блочные конструкторы'],
        category_path=category_path_bases[
            'Главная::Детские игрушки::Детские конструкторы::Блочные конструкторы::Блочные SLUBAN'
        ],
        price=4599,
        url_id='2867791',
        warehouse=None,
        count=None,
        instock=None,
        city=city_bases['msk'],
        updated_at=datetime(2024, 1, 28, 23, 49),
        discount_price=2719,
        razmer=None,
    ),
    Product(
        name='Конструктор LEGO Harry Potter Gryffindor House Banner 76409',
        articul='76409',
        gost=None,
        brand='-',
        category=category_bases['igrushki_i_igry'],
        nomenclature=nomenclature_bases['Блочные конструкторы'],
        category_path=category_path_bases[
            'Главная::Детские игрушки::Детские конструкторы::Блочные конструкторы::Блочные LEGO'
        ],
        price=4999,
        url_id='6041856',
        warehouse=None,
        count=None,
        instock=None,
        city=city_bases['msk'],
        updated_at=datetime(2024, 1, 28, 23, 49),
        discount_price=3599,
        razmer=None,
    ),
    Product(
        name='Конструктор Djeco найди отражение животные',
        articul='06483',
        gost=None,
        brand='-',
        category=category_bases['igrushki_i_igry'],
        nomenclature=nomenclature_bases['Развивающие'],
        category_path=category_path_bases[
            'Главная::Детские игрушки::Настольные игры::Развивающие::Развивающие Djeco'
        ],
        price=4907,
        url_id='6417014',
        warehouse=None,
        count=None,
        instock=None,
        city=city_bases['msk'],
        updated_at=datetime(2024, 1, 28, 23, 57),
        discount_price=4416,
        razmer=None,
    ),
]
