import datetime
from typing import Optional

from app.database import Base
from app.models.category import Category
from app.models.category_path import CategoryPath
from app.models.city import City
from app.models.nomenclature import Nomenclature
from sqlalchemy import DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Product(Base):
    '''Основная таблицы содержащая информацию о продуктах'''

    __tablename__ = 'product'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, comment='Внутренний идентификатор продукта')
    name: Mapped[str] = mapped_column(String(250), comment='Наименования')
    articul: Mapped[str] = mapped_column(String(40), comment='Артикул')
    gost: Mapped[Optional[str]] = mapped_column(String(40), comment='ГОСТ')
    brand: Mapped[Optional[str]] = mapped_column(String(40), comment='БРЕНД')

    category_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(Category.id, ondelete='CASCADE', onupdate='CASCADE'),
        comment='Внутренний идентификатор категории',
    )
    nomenclature_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(Nomenclature.id, ondelete='CASCADE', onupdate='CASCADE'),
        comment='Внутренний идентификатор номенклатуры',
    )
    category_path_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(CategoryPath.id, ondelete='CASCADE', onupdate='CASCADE'),
        comment='Внутренний идентификатор категории пути',
    )
    price: Mapped[float] = mapped_column(comment='Цена')
    url_id: Mapped[str] = mapped_column(
        String(9), comment='id для формирования url на страницу продукта'
    )  # TODO unique=True сделать не удалось из-за дублирования товаров (214547, 8454, ...)

    warehouse: Mapped[Optional[str]] = mapped_column(String(80), comment='Изготовитель')
    instock: Mapped[Optional[str]] = mapped_column(String(40), comment='Складской статус')
    city_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(City.id), comment='Внутренний идентификатор города'
    )
    updated_at: Mapped[datetime] = mapped_column(DateTime, comment='Дата обновления')
    discount_price: Mapped[Optional[float]] = mapped_column(Float, comment='Цена со скидкой')
    razmer: Mapped[Optional[str]] = mapped_column(String(9), comment='Размер')

    city: Mapped[City] = relationship("City", foreign_keys=[city_id], lazy="selectin")
    category_path: Mapped[CategoryPath] = relationship(
        "CategoryPath", foreign_keys=[category_path_id], lazy="selectin"
    )
    nomenclature: Mapped[Nomenclature] = relationship(
        "Nomenclature", foreign_keys=[nomenclature_id], lazy="selectin"
    )
    category: Mapped[Category] = relationship("Category", foreign_keys=[category_id], lazy="selectin")
