"""Tests for hash file use case."""
from unittest.mock import AsyncMock, create_autospec

import pytest

from src.interfaces.repositories.i_hash_repo import IHashRepository
from src.use_cases.hash_files_use_case import HashFilesUseCase


class TestHashFileUseCase(object):
    """Tests for HashFilesUseCase."""

    @pytest.mark.asyncio()
    async def test_execute(
        self: 'TestHashFileUseCase',
        mock_path_to_dir_for_hash: str = '/mock_path',
    ):
        """Testing execute method."""
        mock_repo = create_autospec(IHashRepository)
        mock_repo.get_filenames_with_hashes = AsyncMock()
        await HashFilesUseCase(mock_repo).execute(mock_path_to_dir_for_hash)
        (
            mock_repo.
            get_filenames_with_hashes.
            assert_awaited_once_with(mock_path_to_dir_for_hash)
        )
