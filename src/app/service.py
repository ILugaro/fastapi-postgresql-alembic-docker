from fastapi import FastAPI
from uvicorn import run

import os
from contextlib import asynccontextmanager
from typing import Union

from app import constants
from app.api.router import router
from app.services.parser import ParserService
from app.services.product import ProductService
from settings import Service

dir = os.path.dirname(os.path.abspath(__file__))

class APIService:
    def __init__(self, settings: Union[Service, None] = None) -> None:
        """
        Инициализации ASGI приложения
        """
        self.loop = None
        if settings is None:
            self.settings = Service()

        self.main_app = FastAPI(
            lifespan=check_and_create_db
        )

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
        await ParserService.create_db_from_excel(
            str(os.path.join(dir, '..',  'files', constants.NAME_OF_EXCEL_FILE))
        )
        print(f'Заполнение БД завершено, внесено {await ProductService.count_of_product()} наименований')
    print('Запуск REST API')
    yield


api_service = APIService()
