"""Работа с данныим о продуктах"""
import math
from typing import Literal, Union

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import async_session
from app.models.product import Product


class ProductService:
    """Работа с данныим о продуктах"""

    @staticmethod
    async def count_of_product() -> int:
        """
        Получение количества всех продуктов в БД

        :return: Количество всех продуктов в БД
        """

        async with async_session() as session:
            session: AsyncSession
            async with session.begin():
                query = select(func.count(Product.id))
                return (await session.execute(query)).scalar()

    @staticmethod
    async def get_all_products(
        page: int = 1, limit: int = 10
    ) -> dict[
        Literal["page_number", "page_size", "total_pages", "total_products", "data"],
        Union[int, list[Product]],
    ]:
        """
        Получение с БД всей продукции

        :return: Экземпляры всех продуктов из БД
        """
        async with async_session() as session:
            query = select(Product)

            # пагинация
            offset_page = page - 1
            query = query.offset(offset_page * limit).limit(limit)

            result = await session.execute(query)
            products: list[Product] = result.scalars().all()

            # определение общего числа продуктов и страниц соответствующего лимита
            total_products: int = await ProductService.count_of_product()
            total_page: int = math.ceil(total_products / limit)

        return {
            'page_number': page,
            'page_size': limit,
            'total_pages': total_page,
            'total_products': total_products,
            'data': products,
        }

    @staticmethod
    async def get_product_by_id(product_id: int) -> Product:
        """
        Получение с БД экземпляра продукта по внутреннему PK id

        :param product_id: Внутренний идентификатор продукта
        :return: Экземпляр продукта со всей информацией о нем
        """
        async with async_session() as session:
            query = select(Product).where(Product.id == product_id)
            result = await session.execute(query)
            product = result.scalars().first()
        return product
