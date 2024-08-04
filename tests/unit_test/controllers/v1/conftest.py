"""Conftest for v1 controller."""
import secrets
from typing import List
from unittest.mock import Mock, patch

import pytest

from src.controllers.v1.download_archive_controller import (
    DownloadArchiveControllerV1,
)
from src.domain.file_metadata import FileMetadata


@pytest.fixture()
def download_archive_controller_v1_fixture():
    return DownloadArchiveControllerV1(
        file_repo_type=Mock(),
        hash_repo_type=Mock(),
        http_repo_type=Mock(),
    )


@pytest.fixture()
def repos_metadata_fixture():
    metadata = mock_repo_metadata()
    return [metadata for _ in range(3)]


@pytest.fixture()
def wrong_repos_metadata_fixture():
    repo_metadata = mock_repo_metadata()
    wrong_repo_metadata = mock_repo_metadata()
    return [
        repo_metadata,
        repo_metadata,
        wrong_repo_metadata,
    ]


@pytest.fixture()
def use_cases_fixture():
    paths_to_methods = [
        'src.use_cases.write_file_use_case.WriteFileUseCase.execute',
        'src.use_cases.hash_files_use_case.HashFilesUseCase.execute',
        'src.use_cases.fetch_file_use_case.FetchFileUseCase.execute',
        'src.use_cases.extract_file_use_case.ExtractFileUseCase.execute',
    ]
    with patch(paths_to_methods[0]) as write_file_mock:
        with patch(paths_to_methods[1]) as hash_files_mock:
            with patch(paths_to_methods[2]) as fetch_file_mock:
                with patch(paths_to_methods[3]) as extract_file_mock:
                    yield (
                        write_file_mock,
                        hash_files_mock,
                        fetch_file_mock,
                        extract_file_mock,
                    )


def mock_method(method_patch: str):
    with patch(method_patch) as mock:
        yield mock


def mock_repo_metadata() -> List[FileMetadata]:
    return [
        FileMetadata(
            filename=str(index),
            hash=str(secrets.randbelow(10)),
        )
        for index in range(10)
    ]
