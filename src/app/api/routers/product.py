"""Роут запросов для продуктов"""
from typing import Annotated, Literal, Union

from fastapi import APIRouter, Depends, Path, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app import models, schemas
from app.database import get_async_session
from app.schemas.product import ProductsData
from app.services.product import ProductService

router = APIRouter(prefix='/product')


@router.get(
    '/product/{product_id}',
    response_model=schemas.Product,
    description="Получить продукт по внутреннему идентификатору",
)
async def get_product_by_id(
    product_id: Annotated[int, Path(description="Внутренний идентификатор продукта")],
    session: AsyncSession = Depends(get_async_session),
) -> models.Product:
    """
    Получение с БД экземпляра продукта по внутреннему PK id

    :param product_id: Внутренний идентификатор продукта
    :return: Экземпляр продукта со всей информацией о нем
    """

    return await ProductService.get_product_by_id(session, product_id)


@router.get('/all_products/', response_model=ProductsData, description="Получить всю продукцию")
async def get_all_products(
    page: Annotated[int, Query(description='Страница пагинации', gt=0)] = 1,
    limit: Annotated[int, Query(description='Лимит количества продуктов на страницу', gt=0)] = 10,
    session: AsyncSession = Depends(get_async_session),
) -> dict[
    Literal["page_number", "page_size", "total_pages", "total_products", "data"],
    Union[int, list[models.Product]],
]:
    """
    Получение с БД всех экземпляров продукции

    :param page: Страница пагинации
    :param limit: Лимит количества продуктов на страницу
    :param session: Объект сессии
    :return: Экземпляры всех продуктов в БД
    """

    return await ProductService.get_all_products(session, page, limit)
