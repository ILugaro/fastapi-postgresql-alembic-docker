import os

import pytest

from app import constants, Product
from app.services.parser import ParserService

folder_path = os.path.dirname(os.path.abspath(__file__))
@pytest.mark.asyncio
async def test_create_products_from_excel():
    """Проверка парсинга xmls"""
    products: list[Product] = await ParserService.create_products_from_excel(str(os.path.join(folder_path, '..', 'files', constants.NAME_OF_EXCEL_FILE)))
    assert len(products) == 41147, 'Несоответствие количества продуктов в файле'
    assert products[0].name == 'Конструктор SLUBAN Сапфировый замок'
    assert products[0].articul == 'M38-B0610'
    assert products[0].gost is None
    assert products[0].brand == '-'
    assert products[0].category.category == 'igrushki_i_igry'
    assert products[0].nomenclature.nomenclature == 'Блочные конструкторы'
    assert products[0].category_path.category_path == 'Главная::Детские игрушки::Детские конструкторы::Блочные конструкторы::Блочные SLUBAN'
    assert products[0].price == 4599
    assert products[0].url_id == '2867791'
    assert products[0].warehouse is None
    assert products[0].instock is None
    assert products[0].city.city == 'msk'
    assert products[0].updated_at.year == 2024
    assert products[0].updated_at.month == 1
    assert products[0].updated_at.day == 28
    assert products[0].updated_at.hour == 23
    assert products[0].updated_at.minute == 49
    assert products[0].discount_price == 2719
    assert products[0].razmer is None
