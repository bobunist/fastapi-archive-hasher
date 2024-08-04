"""Tests for write file use case."""
from unittest.mock import AsyncMock, Mock, create_autospec

import pytest

from src.interfaces.repositories.i_file_repo import IFileRepository
from src.use_cases.write_file_use_case import WriteFileUseCase


class TestWriteFileUseCase(object):
    """Tests for WriteFileUseCase."""

    @pytest.mark.asyncio()
    async def test_execute(
        self: 'TestWriteFileUseCase',
    ):
        """Testing execute method."""
        content_generator = Mock()
        mock_repo = create_autospec(IFileRepository)
        mock_repo.write_file = AsyncMock()
        await WriteFileUseCase(mock_repo).execute(content_generator)
        (
            mock_repo.
            write_file.
            assert_awaited_once_with(content_generator)
        )
