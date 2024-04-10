from app.database import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class CategoryPath(Base):
    """Типы путей для категорий"""

    __tablename__ = 'category_path'

    id: Mapped[int] = mapped_column(primary_key=True, comment='Внутренний идентификатор пути категории')
    category_path: Mapped[str] = mapped_column(String(700), comment='Путь категории', unique=True)

