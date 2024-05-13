"""Database configuration"""
from datetime import datetime
from typing import AsyncGenerator, Final

from sqlalchemy import DateTime, MetaData, func
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

from settings import PostgresQL

postgres = PostgresQL()

DATABASE_URL: Final[str] = (
    f"postgresql+asyncpg://"
    f"{postgres.user}:{postgres.password}@{postgres.host}:{postgres.port}/{postgres.database}"
)

engine: AsyncEngine = create_async_engine(DATABASE_URL, future=True)
async_session_maker = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)  # TODO MyPy
metadata = MetaData()


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


class Base(DeclarativeBase):
    """DeclarativeBase configuration"""

    create_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    update_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
