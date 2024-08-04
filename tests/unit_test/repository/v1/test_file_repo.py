"""Testing file repo v1."""
from pathlib import Path
from typing import Any, AsyncGenerator

import pytest
from aiofiles.tempfile.temptypes import AsyncTemporaryDirectory

from src.repository.v1.file_repo import FileRepositoryV1


class TestFileRepository(object):
    """Tests for FileRepositoryV1."""

    @pytest.mark.asyncio()
    async def test_activate_temp_dir(
        self: 'TestFileRepository',
    ):
        """Test activate temp dir."""
        file_repository = FileRepositoryV1(temp_dir='.')
        await file_repository.activate_temp_dir()
        assert isinstance(file_repository.temp_dir, AsyncTemporaryDirectory)

    @pytest.mark.asyncio()
    async def test_write_file(
        self: 'TestFileRepository',
        async_archive_generator_fixture: AsyncGenerator[bytes, Any],
    ):
        """Test for write file from async gen."""
        file_repository = FileRepositoryV1(
            temp_dir='.',
            filename='test_filename',
        )
        file_path = await file_repository.write_file(
            async_archive_generator_fixture,
        )
        assert Path(file_path).is_file()

    @pytest.mark.asyncio()
    async def test_extract_files(
        self: 'TestFileRepository',
        temp_archive_fixture: Path,
    ):
        """Test for extract files from archive."""
        file_repository = FileRepositoryV1()
        await file_repository.extract_files(str(temp_archive_fixture))
