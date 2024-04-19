"""SQL модель номенклатуры"""
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Nomenclature(Base):
    """Типы номенклатуры (например: Блочные конструкторы)"""

    __tablename__ = 'nomenclature'

    id: Mapped[int] = mapped_column(primary_key=True, comment='Внутренний идентификатор номенклатуры')
    nomenclature: Mapped[str] = mapped_column(String(250), comment='Имя номенклатуры', unique=True)
