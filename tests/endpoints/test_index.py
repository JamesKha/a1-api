from httpx import AsyncClient

from app.main import app


async def test_index_endpoint(client: AsyncClient):
    response = await client.get(app.url_path_for("index"))
    assert response.status_code == 200
    assert response.json() == "Hello World!"
