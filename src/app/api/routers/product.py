"""Роут запросов для продуктов"""
from typing import Annotated, Literal, Union

from fastapi import APIRouter, Path

from app import models, schemas
from app.schemas.product import ProductsData
from app.services.product import ProductService

router = APIRouter(prefix='/product')


@router.get(
    '/product/{product_id}',
    response_model=schemas.Product,
    description="Получить продукт по внутреннему идентификатору",
)
async def get_product_by_id(
    product_id: Annotated[int, Path(description="Внутренний идентификатор продукта")]
) -> models.Product:
    """
    Получение с БД экземпляра продукта по внутреннему PK id

    :param product_id: Внутренний идентификатор продукта
    :return: Экземпляр продукта со всей информацией о нем
    """
    return await ProductService.get_product_by_id(product_id)


@router.get('/all_products/', response_model=ProductsData, description="Получить всю продукцию")
async def get_all_products(
    page: Annotated[int, Path(description='Страница пагинации')] = 1,
    limit: Annotated[int, Path(description='Лимит количества продуктов на страницу')] = 10,
) -> dict[
    Literal["page_number", "page_size", "total_pages", "total_products", "data"],
    Union[int, list[models.Product]],
]:
    """
    Получение с БД всех экземпляров продукции

    :param page: Страница пагинации
    :param limit: Лимит количества продуктов на страницу
    :return: Экземпляры всех продуктов в БД
    """

    return await ProductService.get_all_products(page, limit)
