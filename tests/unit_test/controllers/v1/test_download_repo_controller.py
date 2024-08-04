"""Testing v1 controller."""
from contextlib import nullcontext
from typing import ContextManager, List
from unittest.mock import MagicMock

import pytest
from fastapi import HTTPException

from src.controllers.v1.download_archive_controller import (
    DownloadArchiveControllerV1,
)
from src.domain.file_metadata import FileMetadata


class TestDownloadRepoController(object):
    """Test of v1 DownloadRepoController."""

    @pytest.mark.asyncio()
    async def test_execute(
        self: 'TestDownloadRepoController',
        download_archive_controller_v1_fixture: DownloadArchiveControllerV1,
        use_cases_fixture: List[MagicMock],
        mock_url: str = '/mock_url',
    ):
        """Test use cases calls."""
        await download_archive_controller_v1_fixture.execute(mock_url)

        for use_case in use_cases_fixture:
            assert use_case.call_count == 3

    @pytest.mark.asyncio()
    async def test_process_archive(
        self: 'TestDownloadRepoController',
        download_archive_controller_v1_fixture: DownloadArchiveControllerV1,
        use_cases_fixture: List[MagicMock],
        mock_url: str = '/mock_url',
    ):
        """Test use cases calls."""
        await download_archive_controller_v1_fixture.process_archive(mock_url)

        for use_case in use_cases_fixture:
            assert use_case.call_count == 1

    test_assert_hashes_testcases = (
        ('expectation', 'repos_metadata'),
        (
            (nullcontext(), pytest.lazy_fixture('repos_metadata_fixture')),
            (
                pytest.raises(HTTPException),
                pytest.lazy_fixture('wrong_repos_metadata_fixture'),
            ),
        ),
    )

    @pytest.mark.parametrize(
        *test_assert_hashes_testcases,
    )
    @pytest.mark.asyncio()
    async def test_assert_hashes(
        self: 'TestDownloadRepoController',
        expectation: ContextManager,
        repos_metadata: List[List[FileMetadata]],
        download_archive_controller_v1_fixture: DownloadArchiveControllerV1,
    ):
        """Test error handling when different hashes.

        Из-за WPS441 нельзя проверять ошибку.
        После ее выбрасывания код внутри менеджера не идет дальше.
        Использование try/except не подходит,
        поскольку к exception_info.value можно обратиться
        только после закрытия менеджера.
        """
        with expectation:
            download_archive_controller_v1_fixture.assert_hashes(
                repos_metadata,
            )
