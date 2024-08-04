"""Module with extract file use case."""

from src.interfaces.repositories.i_file_repo import IFileRepository


class ExtractFileUseCase(object):
    """Write file use case."""

    def __init__(
        self: 'ExtractFileUseCase',
        file_repo: IFileRepository,
    ) -> None:
        """Define repos for use cases."""
        self.file_repo = file_repo

    async def execute(
        self: 'ExtractFileUseCase',
        path_to_archive: str,
    ) -> str:
        """Extract file and return its path."""
        return await self.file_repo.extract_files(path_to_archive)
