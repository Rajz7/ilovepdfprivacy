from fastapi import APIRouter
from app.api.routes import compress, merge, split, convert

api_router = APIRouter()

api_router.include_router(compress.router, prefix="/pdf", tags=["pdf"])
api_router.include_router(merge.router, prefix="/pdf", tags=["pdf"])
api_router.include_router(split.router, prefix="/pdf", tags=["pdf"])
api_router.include_router(convert.router, tags=["convert"])
