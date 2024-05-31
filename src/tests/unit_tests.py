"""Юнит тесты"""
import os

import pytest
from httpx import AsyncClient

from app import Product
from app.services.parser import ParserService
from tests import test_data

folder_path = os.path.dirname(os.path.abspath(__file__))


async def test_create_products_from_file():
    """Проверка парсинга xmls"""
    products: list[Product] = await ParserService.create_products_from_excel(
        str(os.path.join(folder_path, 'test_data', 'test_detskiymir_msk_products.xlsx'))
    )
    assert len(products) == 41147, 'Несоответствие количества продуктов в файле'

    # проверка продукта со всеми заполненными полями
    assert products[0].name == 'Конструктор SLUBAN Сапфировый замок'
    assert products[0].articul == 'M38-B0610'
    assert products[0].gost == 'ТУ 17.23.13-004'
    assert products[0].brand == 'LEGO'
    assert products[0].category.category == 'igrushki_i_igry'
    assert products[0].nomenclature.nomenclature == 'Блочные конструкторы'
    assert (
        products[0].category_path.category_path
        == 'Главная::Детские игрушки::Детские конструкторы::Блочные конструкторы::Блочные SLUBAN'
    )
    assert products[0].price == 4599
    assert products[0].url_id == '2867791'
    assert products[0].warehouse == 'Lego & co'
    assert products[0].count == 16
    assert products[0].instock == 'ожидается'
    assert products[0].city.city == 'msk'
    assert products[0].updated_at.year == 2024
    assert products[0].updated_at.month == 1
    assert products[0].updated_at.day == 28
    assert products[0].updated_at.hour == 23
    assert products[0].updated_at.minute == 49
    assert products[0].discount_price == 2719
    assert products[0].razmer == '19х19х25'

    # проверка продукта с незаполненными обязательными атрибутами
    assert products[41146].name == 'Конструктор Djeco найди отражение животные'
    assert products[41146].articul == '06483'
    assert products[41146].gost is None
    assert products[41146].brand == '-'
    assert products[41146].category.category == 'igrushki_i_igry'
    assert products[41146].nomenclature.nomenclature == 'Развивающие'
    assert (
        products[41146].category_path.category_path
        == 'Главная::Детские игрушки::Настольные игры::Развивающие::Развивающие Djeco'
    )
    assert products[41146].price == 4907
    assert products[41146].url_id == '6417014'
    assert products[41146].warehouse is None
    assert products[41146].count is None
    assert products[41146].instock is None
    assert products[41146].city.city == 'msk'
    assert products[41146].updated_at.year == 2024
    assert products[41146].updated_at.month == 1
    assert products[41146].updated_at.day == 28
    assert products[41146].updated_at.hour == 23
    assert products[41146].updated_at.minute == 57
    assert products[41146].discount_price == 4416
    assert products[41146].razmer is None


async def test_get_product_by_id(ac: AsyncClient):
    """Проверка продукта со всеми заполненными атрибутами"""
    response = await ac.get("/api/product/product/1")
    assert response.status_code == 200

    product = response.json()
    assert product['id'] == 1
    assert product['name'] == 'Конструктор SLUBAN Сапфировый замок'
    assert product['articul'] == 'M38-B0610'
    assert product['gost'] == 'ТУ 17.23.13-004'
    assert product['brand'] == 'LEGO'
    assert product['category'] == {'category': 'igrushki_i_igry', 'id': 1}
    assert product['nomenclature'] == {'nomenclature': 'Блочные конструкторы', 'id': 1}
    assert product['category_path'] == {
        'category_path': 'Главная::Детские игрушки::Детские конструкторы::Блочные конструкторы::Блочные SLUBAN',
        'id': 1,
    }
    assert product['price'] == 4599
    assert product['url_id'] == '2867791'
    assert product['warehouse'] == 'Lego & co'
    assert product['count'] == 16
    assert product['instock'] == 'ожидается'
    assert product['city'] == {'city': 'msk', 'id': 1}
    assert product['updated_at'] == '2024-01-28T23:49:00'
    assert product['discount_price'] == 2719
    assert product['razmer'] == '19х19х25'
    assert product['url'] == 'https://www.detmir.ru/product/index/id2867791/'


async def test_get_product_by_id(ac: AsyncClient):
    """Проверка продукта с пустыми не обязательными атрибутами"""
    response = await ac.get("/api/product/product/4")
    assert response.status_code == 200

    product = response.json()
    assert product['id'] == 4
    assert product['name'] == 'Конструктор Djeco найди отражение животные'
    assert product['articul'] == '06483'
    assert product['gost'] is None
    assert product['brand'] == '-'
    assert product['category'] == {'category': 'igrushki_i_igry', 'id': 1}
    assert product['nomenclature'] == {'nomenclature': 'Развивающие', 'id': 2}
    assert product['category_path'] == {
        'category_path': 'Главная::Детские игрушки::Настольные игры::Развивающие::Развивающие Djeco',
        'id': 3,
    }
    assert product['price'] == 4907
    assert product['url_id'] == '6417014'
    assert product['warehouse'] is None
    assert product['count'] is None
    assert product['instock'] is None
    assert product['city'] == {'city': 'msk', 'id': 1}
    assert product['updated_at'] == '2024-01-28T23:57:00'
    assert product['razmer'] is None


async def test_get_all_products(ac: AsyncClient):
    """Проверка с дефолтными параметрами"""
    response = await ac.get('/api/product/all_products/')

    assert response.status_code == 200

    products = response.json()['data']
    default_limit = 10  # ожидаемый лимит продуктов на странице по умолчанию
    assert (
        len(products) == len(test_data.products)
        if len(test_data.products) < default_limit
        else default_limit
    )


@pytest.mark.parametrize(
    "page, limit, expected_first_id, expected_count", [[1, 2, 1, 2], [2, 2, 3, 2], [4, 1, 4, 1]]
)
async def test_get_all_products(ac: AsyncClient, page, limit, expected_first_id, expected_count):
    """Проверка пагинации и лимита"""
    response = await ac.get('/api/product/all_products/', params={'page': page, 'limit': limit})
    assert response.status_code == 200
    products = response.json()['data']
    assert products[0]['id'] == expected_first_id
    assert len(products) == expected_count
