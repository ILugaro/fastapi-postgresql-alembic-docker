"""ASGI"""
import os
from contextlib import asynccontextmanager
from typing import Union

from fastapi import FastAPI
from uvicorn import run

from app import constants
from app.api.router import router
from app.database import async_session_maker
from app.models.product import Product
from app.services.parser import ParserService
from app.services.product import ProductService
from settings import Service

folder_path = os.path.dirname(os.path.abspath(__file__))


class APIService:
    """ASGI"""

    def __init__(self, settings: Union[Service, None] = None) -> None:
        """
        Инициализации ASGI приложения
        """
        self.loop = None
        if settings is None:
            self.settings = Service()

        self.main_app = FastAPI(lifespan=check_and_create_db)

        self.main_app.include_router(router)

    def get_app(self) -> FastAPI:
        """
        Получение ASGI приложения

        :return: None
        """
        return self.main_app

    def serve(self, path_to_app: str) -> None:
        """
        Запуск сервиса

        :return: None
        """
        run(path_to_app, host=self.settings.host, port=self.settings.port, reload=True, use_colors=True)


@asynccontextmanager
async def check_and_create_db(app: FastAPI):
    """
    Инициализация заполнения БД если она пуста до начала работы API

    :return: None
    """

    if await ProductService.count_of_product() == 0:
        print('Начато заполнение пустой БД (первый запуск)')
        # парсинг Excel документа
        products: list[Product] = await ParserService.create_products_from_excel(
            str(os.path.join(folder_path, '..', 'files', constants.NAME_OF_EXCEL_FILE))
        )
        # внесение полученных продуктов в БД
        async with async_session_maker() as session:
            session.add_all(products)
            await session.commit()

        print(f'Заполнение БД завершено, внесено {await ProductService.count_of_product()} наименований')
    print('Запуск REST API')
    yield


api_service = APIService()
