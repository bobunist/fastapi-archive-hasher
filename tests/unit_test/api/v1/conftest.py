"""Conftest for v1 router."""

import secrets
from typing import List
from unittest.mock import AsyncMock, Mock

import pytest

from src.domain.file_metadata import FileMetadata


@pytest.fixture()
def download_repo_controller_fixture():
    download_repo_controller = Mock()
    download_repo_controller.execute = AsyncMock(
        return_value=mock_file_metadata(),
    )
    return download_repo_controller


def mock_file_metadata() -> List[FileMetadata]:
    return [
        FileMetadata(
            filename=str(index),
            hash=str(secrets.randbelow(10)),
        ) for index in range(10)
    ]
