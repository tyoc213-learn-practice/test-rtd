from fastapi import APIRouter

from app.api.sueldo.sueldo import router as sueldo_router


router = APIRouter()


router.include_router(sueldo_router, prefix="/sueldo", tags=["sueldo"])

