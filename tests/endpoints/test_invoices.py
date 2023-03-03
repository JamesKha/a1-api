from httpx import AsyncClient

from app.main import app


async def test_invoices_create_endpoint(client: AsyncClient, sample_invoice):
    response = await client.post(
        app.url_path_for("create_invoice"), data=sample_invoice
    )
    # TODO Currently, the status code is 422 (Unprocessable Entity) because the
    # expected request object has no attributes, whereas the actual sample
    # invoice has many!
    assert response.status_code == 201
    assert response.json() == sample_invoice


# TODO Complete other tests here
