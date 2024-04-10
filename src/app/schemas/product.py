from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, computed_field

from app import constants, schemas


class Product(BaseModel):
    """Схема продукта для отправки по REST API"""

    id: int
    name: str
    articul: str
    gost: Optional[str]
    brand: Optional[str]
    category: schemas.Category
    nomenclature: schemas.Nomenclature
    category_path: schemas.CategoryPath
    price: float
    url_id: str
    warehouse: Optional[str]
    instock: Optional[str]
    city: schemas.City
    updated_at: datetime
    discount_price: Optional[float]
    razmer: Optional[str]

    @computed_field
    @property
    def url(self) -> str:
        """Формирование url по id продукта на сайте"""
        return constants.URL_PATH_FOR_PRODUCT + self.url_id + '/'

    class Config:
        from_attributes = True  # формируется на основе данных из SQL


@dataclass
class ProductsData:
    """Информация о продуктах в form-data"""
    data: list[Product]
