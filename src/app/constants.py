"""Переменные с константными значениями"""
from typing import Final

URL_PATH_FOR_PRODUCT: Final[
    str
] = r'https://www.detmir.ru/product/index/id'  # путь для подстановки id товара

NAME_OF_EXCEL_FILE: Final[str] = 'detskiymir_msk_products.xlsx'


# *нумерация столбцов и строк начинается с единицы
FIRST_DATA_ROW_IN_XLSX: Final[
    int
] = 2  # с какой строки в excel документе начинаются строки продуктов (включительно)

# нумерация колонок
NAME_COL: Final[int] = 1
ARTICUL_COL: Final[int] = 2
GOST_COL: Final[int] = 3
BRAND_COL: Final[int] = 4
CATEGORY_COL: Final[int] = 5
NOMENCLATURE_COL: Final[int] = 6
CATEGORY_PATH_COL: Final[int] = 7
PRICE_COL: Final[int] = 8
URL_COL: Final[int] = 9
WAREHOUSE_COL: Final[int] = 10
COST: Final[int] = 11
INSTOCK_COL: Final[int] = 12
CITY_COL: Final[int] = 13
UPDATED_AT_COL: Final[int] = 14
DISCOUNT_PRICE_COL: Final[int] = 15
RAZMER_COL: Final[int] = 16

# Errors
NOT_EXPECTED_URL: Final[str] = 'Указанный URL {} имеет не ожидаемый формат. Продукт {}'
NOT_URL: Final[str] = 'Продукт {} не имеет URL'
