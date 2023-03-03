import logging

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def index() -> str:
    """An index endpoint that always returns HTTP 200"""
    logging.debug("New request")
    return "Hello World!"
