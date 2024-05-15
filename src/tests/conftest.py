"""Конфигурация pytest"""
from typing import AsyncGenerator, Final

import pytest
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.database import get_async_session, metadata
from settings import PostgreSQLTest
from main import app

postgres = PostgreSQLTest()

DATABASE_URL: Final[str] = (
    f"postgresql+asyncpg://"
    f"{postgres.user}:{postgres.password}@{postgres.host}:{postgres.port}/{postgres.database}"
)

engine_test: AsyncEngine = create_async_engine(DATABASE_URL, future=True)
async_session_maker = sessionmaker(engine_test, expire_on_commit=False, class_=AsyncSession)  # TODO MyPy
metadata.bind = engine_test


async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """Создание SQL сессии тестовой БД"""
    async with async_session_maker() as session:
        yield session


app.dependency_overrides[get_async_session] = override_get_async_session


@pytest.fixture(autouse=True, scope='session')
async def prepare_database():
    """Подготовка БД к тестированию"""
    async with engine_test.begin() as conn:
        await conn.run_sync(metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(metadata.drop_all)
