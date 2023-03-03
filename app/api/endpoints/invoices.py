import logging

from fastapi import APIRouter, status

from app.schemas.requests import InvoiceCreateRequest, PayOutstandingBalanceRequest
from app.schemas.responses import (
    GetBalanceResponse,
    InvoiceCreateResponse,
    PayOutstandingBalanceResponse,
)

router = APIRouter()

# In-memory invoice store
INVOICES = list()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_invoice(invoice: InvoiceCreateRequest) -> InvoiceCreateResponse:
    """An endpoint for creating invoices"""
    logging.debug(f"New request (POST /): {invoice}")
    # TODO Instantiate an invoice object and store it in INVOICES
    return InvoiceCreateResponse()


@router.get("/", status_code=status.HTTP_200_OK)
async def get_balance() -> GetBalanceResponse:
    """An endpoint calculating the invoices' outstanding balance"""
    logging.debug("New request (GET invoices/balance)")
    return GetBalanceResponse()


@router.put("/pay", status_code=status.HTTP_200_OK)
async def pay_outstanding_balance(
    request: PayOutstandingBalanceRequest,
) -> PayOutstandingBalanceResponse:
    """An endpoint for paying outstanding balance"""
    logging.debug(f"New request (GET invoices/pay): {request}")
    return PayOutstandingBalanceResponse()
