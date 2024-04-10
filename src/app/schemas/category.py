from pydantic import BaseModel

class Category(BaseModel):
    """Типы категорий продуктов (Например: igrushki_i_igry)"""
    id: int
    category: str

    class Config:
        from_attributes = True  # формируется на основе данных из SQL



