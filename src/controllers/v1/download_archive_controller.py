"""Module with v1 DownloadRepositoryController."""
import asyncio
from typing import List, Type

from fastapi import HTTPException, status

from src.controllers.v1.dependencies import (
    FileRepositoryType,
    HashRepositoryType,
    HttpRepositoryType,
)
from src.domain.file_metadata import FileMetadata
from src.interfaces.i_controller import IController
from src.use_cases.extract_file_use_case import ExtractFileUseCase
from src.use_cases.fetch_file_use_case import FetchFileUseCase
from src.use_cases.hash_files_use_case import HashFilesUseCase
from src.use_cases.write_file_use_case import WriteFileUseCase


class DownloadArchiveControllerV1(IController):
    """Realization of IDownloadRepositoryController."""

    def __init__(
        self: 'DownloadArchiveControllerV1',
        file_repo_type: Type[FileRepositoryType] = FileRepositoryType,
        hash_repo_type: Type[HashRepositoryType] = HashRepositoryType,
        http_repo_type: Type[HttpRepositoryType] = HttpRepositoryType,
    ) -> None:
        """Define repos for use cases."""
        self.file_repo_type = file_repo_type
        self.hash_repo_type = hash_repo_type
        self.http_repo_type = http_repo_type

    async def execute(
        self: 'DownloadArchiveControllerV1',
        url: str,
    ) -> List[FileMetadata]:
        """Download archive, check hashes and return if correct."""
        tasks = [
            self.process_archive(url) for _ in range(3)
        ]
        repos_metadata: List[List[FileMetadata]] = await asyncio.gather(*tasks)
        return self.assert_hashes(repos_metadata)

    async def process_archive(
        self: 'DownloadArchiveControllerV1',
        url: str,
    ) -> List[FileMetadata]:
        """Download archive, write it locally and return files metadata."""
        file_repo = self.file_repo_type()

        content_generator = await FetchFileUseCase(
            self.http_repo_type(),
        ).execute(url)

        path_to_archive = await WriteFileUseCase(
            file_repo,
        ).execute(content_generator)

        dir_for_hash = await ExtractFileUseCase(
            file_repo,
        ).execute(path_to_archive)

        return await HashFilesUseCase(
            self.hash_repo_type(),
        ).execute(dir_for_hash)

    def assert_hashes(
        self: 'DownloadArchiveControllerV1',
        repos_metadata: List[List[FileMetadata]],
    ) -> List[FileMetadata]:
        """Assert hashes in extracted archive."""
        for first, second, third in zip(*repos_metadata):
            if first.hash == second.hash == third.hash:
                continue
            raise HTTPException(
                detail=[
                    'Wrong downloading',
                    first.hash,
                    second.hash,
                    third.hash,
                ],
                status_code=status.HTTP_409_CONFLICT,
            )
        return repos_metadata[0]
