"""Response classes."""
from pydantic import BaseModel


class BaseResponse(BaseModel):
    pass


class InvoiceCreateResponse(BaseResponse):
    # TODO Complete this class
    pass


class GetBalanceResponse(BaseResponse):
    # TODO Complete this class
    pass


class PayOutstandingBalanceResponse(BaseResponse):
    # TODO Complete this class
    pass
