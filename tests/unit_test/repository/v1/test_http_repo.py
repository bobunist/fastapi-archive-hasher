"""Testing http repo v1."""
from typing import AsyncGenerator

import pytest

from src.config import Settings
from src.repository.v1.http_repo import HttpRepositoryV1


class TestHttpRepository(object):
    """Tests for HttpRepositoryV1."""

    @pytest.mark.asyncio()
    async def test_fetch(
        self: 'TestHttpRepository',
    ):
        """Test get async gen with file from url."""
        file_generator = HttpRepositoryV1().fetch(
            Settings().repo_url,
        )
        assert isinstance(file_generator, AsyncGenerator)
