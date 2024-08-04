"""Module with hash repo interface."""

from abc import ABC, abstractmethod
from typing import List

from src.domain.file_metadata import FileMetadata


class IHashRepository(ABC):
    """Interface for hash repo."""

    @abstractmethod
    async def get_filenames_with_hashes(
        self: 'IHashRepository',
        root_dir: str,
    ) -> List[FileMetadata]:
        """Get hash of dir content."""
        raise NotImplementedError
