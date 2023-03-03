"""Request classes."""
from pydantic import BaseModel


class BaseRequest(BaseModel):
    pass


class InvoiceCreateRequest(BaseRequest):
    # TODO Complete this class
    pass


class PayOutstandingBalanceRequest(BaseRequest):
    # TODO Complete this class
    pass
