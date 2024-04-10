

from pydantic import BaseModel
class City(BaseModel):
    """Города"""

    id: int
    city: str

    class Config:
        from_attributes = True  # формируется на основе данных из SQL


