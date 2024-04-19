"""Pydantic модель номенклатуры"""
from pydantic import BaseModel


class Nomenclature(BaseModel):
    """Номенклатура"""

    id: int
    nomenclature: str

    class Config:
        """Конфигурация модели"""

        from_attributes = True  # формируется на основе данных из SQL
