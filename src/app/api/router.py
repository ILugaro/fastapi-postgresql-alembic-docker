from fastapi import APIRouter

from app.api.routers import product


router = APIRouter(prefix='/api')

router.include_router(product.router)
