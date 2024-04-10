from pydantic import BaseModel


class Nomenclature(BaseModel):
    """Номенклатура"""

    id: int
    nomenclature: str

    class Config:
        from_attributes = True  # формируется на основе данных из SQL

