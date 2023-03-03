from fastapi import APIRouter

from app.api.endpoints import index, invoices

api_router = APIRouter()
api_router.include_router(index.router, prefix="", tags=["index"])
api_router.include_router(invoices.router, prefix="/invoices", tags=["invoices"])
