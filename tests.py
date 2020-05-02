import pytest
from app import app


@pytest.mark.asyncio
async def test_home(client):
    response = await client.get('/')
    assert response.status_code == 200
