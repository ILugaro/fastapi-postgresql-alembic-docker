"""Конфигурация pytest"""
import asyncio
import os
from typing import AsyncGenerator, Final

import pytest
from _pytest.monkeypatch import MonkeyPatch
from alembic import command
from alembic.config import Config
from httpx import AsyncClient

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from starlette.testclient import TestClient

from app.database import Base, get_async_session, metadata
from main import app
from settings import PostgreSQLTest
from tests.test_data import products

folder_path = os.path.dirname(os.path.abspath(__file__))

postgres = PostgreSQLTest()

DATABASE_URL: Final[str] = (
    f"postgresql+asyncpg://"
    f"{postgres.user}:{postgres.password}@{postgres.host}:{postgres.port}/{postgres.database}"
)

engine_test: AsyncEngine = create_async_engine(DATABASE_URL, future=True, poolclass=NullPool)
async_session_maker = sessionmaker(engine_test, expire_on_commit=False, class_=AsyncSession)  # TODO MyPy
metadata.bind = engine_test


async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """Создание SQL сессии тестовой БД"""
    async with async_session_maker() as session:
        yield session


app.dependency_overrides[get_async_session] = override_get_async_session


def run_alembic_upgrade(connection, cfg):
    """Апгрейд до последней миграции"""
    cfg.attributes["connection"] = connection
    command.upgrade(cfg, "head")


def run_alembic_downgrade(connection, cfg):
    """Откат всех миграций"""
    cfg.attributes["connection"] = connection
    command.downgrade(cfg, "base")


@pytest.fixture(autouse=True, scope='session')
async def create_database():
    """Подготовка БД к тестированию"""
    mpatch = MonkeyPatch()
    mpatch.setenv('DATABASE_URL', DATABASE_URL)
    config = Config(str(os.path.join(folder_path, '..', 'alembic.ini')))
    config.set_main_option("script_location", str(os.path.join(folder_path, '..', 'migrations')))
    config.set_main_option('sqlalchemy.url', DATABASE_URL)
    async with engine_test.begin() as conn:

        # удаление всех таблиц в БД которые могли остаться с прошлого тестирования
        await conn.run_sync(Base.metadata.drop_all)
        await conn.execute(text('DROP TABLE IF EXISTS alembic_version;'))
        await conn.execute(text('COMMIT;'))

        # проверка отката миграции
        await conn.run_sync(run_alembic_upgrade, config)
        await conn.run_sync(run_alembic_downgrade, config)
        await conn.run_sync(run_alembic_upgrade, config)


        # Наполнение БД тестовыми данными
        async with async_session_maker() as session:
            session.add_all(products.products)
            await session.commit()

        yield

        # удаление всех таблиц в БД после тестирования
        await conn.run_sync(Base.metadata.drop_all)
        await conn.execute(text('DROP TABLE IF EXISTS alembic_version;'))
        await conn.execute(text('COMMIT;'))

@pytest.fixture(scope='session')
def event_loop(request):
    """Создание экземпляра цикла событий для каждого теста"""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


client = TestClient(app)


@pytest.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    """Создание тестового REST API клиента"""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
