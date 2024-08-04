"""Tests for v1 router."""

import pytest

from src.api.v1.router import download_archive_v1
from src.controllers.v1.download_archive_controller import (
    DownloadArchiveControllerV1,
)
from src.domain.file_metadata import FileMetadata


@pytest.mark.asyncio()
async def test_download_repo(
    download_repo_controller_fixture: DownloadArchiveControllerV1,
):
    file_metadata_list = await download_archive_v1(
        download_repo_controller_fixture,
    )
    assert isinstance(file_metadata_list, list)
    assert all(
        isinstance(
            file_metadata, FileMetadata,
        ) for file_metadata in file_metadata_list
    )
