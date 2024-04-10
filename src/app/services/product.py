from sqlalchemy import select


from app.database import async_session
from app.models.product import Product
from sqlalchemy.ext.asyncio import AsyncSession


class ProductService:

    @staticmethod
    async def get_all_products() -> list[Product]:
        """
        Получение с БД всей продукции

        :return: Экземпляры всех продуктов из БД
        """
        async with async_session() as session:
            query = select(Product)
            result = await session.execute(query)
            products = result.scalars().all()
        return products

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

    @staticmethod
    async def count_of_product() -> int:
        """
        Получение количества всех продуктов в БД

        :return: Количество всех продуктов в БД
        """
        from sqlalchemy import func
        async with async_session() as session:
            session: AsyncSession
            async with session.begin():
                query = select(func.count(Product.id))
                return (await session.execute(query)).scalar()
