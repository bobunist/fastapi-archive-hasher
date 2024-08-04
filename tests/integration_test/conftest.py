"""Fixtures for integration tests."""

import pytest
from fastapi.testclient import TestClient

from src.main import app


@pytest.fixture()
def client_fixture():
    return TestClient(app)
