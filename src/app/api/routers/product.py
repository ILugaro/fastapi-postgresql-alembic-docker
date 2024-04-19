"""Роут запросов для продуктов"""
from typing import Annotated, Literal

from fastapi import APIRouter, Path

from app.schemas.product import Product, ProductsData
from app.services.product import ProductService

router = APIRouter(prefix='/product')


@router.get(
    '/product/{product_id}', response_model=Product, description="Получить продукт по идентификатору БД"
)
async def get_all_products(product_id: Annotated[int, Path(description="Идентификатору БД")]) -> Product:
    """
    Получение с БД экземпляра продукта по внутреннему PK id

    :param product_id: Внутренний идентификатор продукта
    :return: Экземпляр продукта со всей информацией о нем
    """
    return await ProductService.get_product_by_id(product_id)


@router.get('/all_products/', response_model=ProductsData, description="Получить всю продукцию")
async def get_product_by_id() -> dict[Literal["data"], list[Product]]:
    """
    Получение с БД всех экземпляров продукции

    :return: Экземпляры всех продуктов в БД
    """
    return {'data': await ProductService.get_all_products()}
