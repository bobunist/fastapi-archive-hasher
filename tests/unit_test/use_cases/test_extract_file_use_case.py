"""Tests for extract file use case."""
from unittest.mock import AsyncMock, create_autospec

import pytest

from src.interfaces.repositories.i_file_repo import IFileRepository
from src.use_cases.extract_file_use_case import ExtractFileUseCase


class TestExtractFileUseCase(object):
    """Tests for ExtractFileUseCase."""

    @pytest.mark.asyncio()
    async def test_execute(
        self: 'TestExtractFileUseCase',
        mock_path_to_archive: str = '/mock_path',
    ):
        """Testing execute method."""
        mock_repo = create_autospec(IFileRepository)
        mock_repo.extract_files = AsyncMock()
        await ExtractFileUseCase(mock_repo).execute(mock_path_to_archive)
        mock_repo.extract_files.assert_awaited_once_with(mock_path_to_archive)
