"""Module with hash file use case."""

from typing import List

from src.domain.file_metadata import FileMetadata
from src.interfaces.repositories.i_hash_repo import IHashRepository


class HashFilesUseCase(object):
    """Hash files in dir use case."""

    def __init__(
        self: 'HashFilesUseCase',
        hash_repo: IHashRepository,
    ) -> None:
        """Define repos for use cases."""
        self.hash_repo = hash_repo

    async def execute(
        self: 'HashFilesUseCase',
        path_to_dir_for_hash: str,
    ) -> List[FileMetadata]:
        """Get filename and hash of files in dir."""
        return await self.hash_repo.get_filenames_with_hashes(
            path_to_dir_for_hash,
        )
