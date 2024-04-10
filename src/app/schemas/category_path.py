
from pydantic import BaseModel

class CategoryPath(BaseModel):
    """Типы путей для категорий"""

    id: int
    category_path: str


    class Config:
        from_attributes = True  # формируется на основе данных из SQL