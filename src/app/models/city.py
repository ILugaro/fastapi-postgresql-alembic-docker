"""SQL модель городов"""
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class City(Base):
    """Таблица городов"""

    __tablename__ = 'city'

    id: Mapped[int] = mapped_column(primary_key=True, comment='Внутренний идентификатор города')
    city: Mapped[str] = mapped_column(String(10), comment='Имя города', unique=True)
