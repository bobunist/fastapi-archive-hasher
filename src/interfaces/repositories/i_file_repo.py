"""Module with file repo interface."""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import AsyncGenerator


class IFileRepository(ABC):
    """Interface for file repo."""

    def __init__(
        self: 'IFileRepository',
        temp_dir: str | Path | None = None,
        filename: str | None = None,
    ) -> None:
        """Fields for subsequent use."""
        self.temp_dir = temp_dir
        self.filename = filename

    @abstractmethod
    async def write_file(
        self: 'IFileRepository',
        content_generator: AsyncGenerator[bytes, None],
    ) -> str:
        """Write file locally."""
        raise NotImplementedError

    @abstractmethod
    async def extract_files(
        self: 'IFileRepository',
        path_to_file: str,
    ) -> str:
        """Extract files from archive."""
        raise NotImplementedError
