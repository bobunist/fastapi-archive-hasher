"""Tests for fetch file use case."""
from unittest.mock import Mock, create_autospec

import pytest

from src.interfaces.repositories.i_http_repo import IHttpRepository
from src.use_cases.fetch_file_use_case import FetchFileUseCase


class TestFetchFileUseCase(object):
    """Tests for FetchFileUseCase."""

    @pytest.mark.asyncio()
    async def test_execute(
        self: 'TestFetchFileUseCase',
        mock_url: str = '/mock_url',
    ):
        """Testing execute method.

        assert_called_once_with instead of
        assert_awaited_once_with because
        use-case should return async gen,
        not coroutine.
        """
        mock_repo = create_autospec(IHttpRepository)
        mock_repo.fetch = Mock()
        await FetchFileUseCase(mock_repo).execute(mock_url)
        mock_repo.fetch.assert_called_once_with(mock_url)
