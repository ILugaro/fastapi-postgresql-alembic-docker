from app.database import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Category(Base):
    """Типы категорий продуктов (Например: igrushki_i_igry)"""

    __tablename__ = 'category'

    id: Mapped[int] = mapped_column(primary_key=True, comment='Внутренний идентификатор категорий')
    category: Mapped[str] = Column(String(40), comment='Тип категории', unique=True)

