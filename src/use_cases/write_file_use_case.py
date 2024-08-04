"""Module with write file use case."""
from typing import AsyncGenerator

from src.interfaces.repositories.i_file_repo import IFileRepository


class WriteFileUseCase(object):
    """Write file use case."""

    def __init__(
        self: 'WriteFileUseCase',
        file_repo: IFileRepository,
    ) -> None:
        """Define repos for use cases."""
        self.file_repo = file_repo

    async def execute(
        self: 'WriteFileUseCase',
        content_generator: AsyncGenerator[bytes, None],
    ) -> str:
        """Write file and return its path."""
        return await self.file_repo.write_file(content_generator)
