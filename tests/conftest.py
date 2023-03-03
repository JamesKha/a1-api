"""
Used to execute code before running tests.

Put here any Pytest related code (it will be executed before `tests/...`)
"""

import os
from collections.abc import AsyncGenerator

import pytest
import pytest_asyncio
from httpx import AsyncClient

from app.main import app

os.environ["ENVIRONMENT"] = "PYTEST"


@pytest_asyncio.fixture
async def client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as client:
        client.headers.update({"Host": "localhost"})
        yield client


@pytest.fixture
def sample_invoice() -> dict:
    return {
        "DueDate": "2023-03-05",
        "DocNumber": "DOC199",
        "Status": "Payable",
        "Line": [
            {
                "Description": "Other Expenses",
                "Amount": 500,
                "ExpenseDetail": {
                    "Customer": {
                        "value": "ABC123",
                        "name": "Metaverse Computing, Inc.",
                    },
                    "Ref": {"value": "DEF234", "name": "Consulting Services"},
                    "Account": {"value": "EFG345", "name": "Fuel"},
                },
            },
            {
                "Description": "Legal Services",
                "Amount": 1432.95,
                "ExpenseDetail": {
                    "Customer": {
                        "value": "ABC123",
                        "name": "Metaverse Computing, Inc.",
                    },
                    "Ref": {"value": "DEF234", "name": "Consulting Services"},
                    "Account": {"value": "EFG346", "name": "Services"},
                },
            },
        ],
        "Vendor": {"value": "ABC999", "name": "ScotiaBank"},
        "APRef": {"value": "XYZ123", "name": "Accounts Payable"},
    }
