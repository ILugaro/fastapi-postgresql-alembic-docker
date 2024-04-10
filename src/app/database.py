from sqlalchemy import DateTime, MetaData, func
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

from datetime import datetime

from settings import PostgresQL


postgres = PostgresQL()

DATABASE_URL = "postgresql+asyncpg://{}:{}@{}:{}/{}".format(
    postgres.user, postgres.password, postgres.host, postgres.port, postgres.database
)
engine = create_async_engine(DATABASE_URL, future=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
metadata = MetaData()

class Base(DeclarativeBase):
    create_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    update_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
