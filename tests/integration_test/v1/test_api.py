"""Tests for v1 router."""
from fastapi import status
from fastapi.testclient import TestClient


def test_download_repo(client_fixture: TestClient):
    """Test response code and returning values."""
    response = client_fixture.get('/v1/download')
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), list)
