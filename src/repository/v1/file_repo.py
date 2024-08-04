"""Module with file repo."""

import asyncio
import uuid
from pathlib import Path
from typing import AsyncGenerator
from zipfile import ZipFile

import aiofiles
from aiofiles.tempfile import AiofilesContextManagerTempDir, TemporaryDirectory

from src.interfaces.repositories.i_file_repo import IFileRepository
from src.utils.thread_pool_singleton import ThreadPoolSingleton


class FileRepositoryV1(IFileRepository):
    """File repo implementation."""

    def __init__(
        self: 'FileRepositoryV1',
        temp_dir: str | Path | None = None,
        filename: str | None = None,
    ) -> None:
        """Fields for internal use from super."""
        super().__init__(temp_dir, filename)

        if temp_dir is None:
            self.temp_dir = TemporaryDirectory(dir=Path.cwd() / '.tmp')
        else:
            self.temp_dir = TemporaryDirectory(dir=temp_dir)

        if filename is None:
            self.filename = str(uuid.uuid4())
        else:
            self.filename = filename

    async def activate_temp_dir(
        self: 'FileRepositoryV1',
    ) -> None:
        """Before use other methods must activate temp dir."""
        if isinstance(self.temp_dir, AiofilesContextManagerTempDir):
            self.temp_dir = await self.temp_dir

    async def write_file(
        self: 'FileRepositoryV1',
        content_generator: AsyncGenerator[bytes, bytes],
    ) -> str:
        """Create temporary dir locally and write file."""
        await self.activate_temp_dir()
        file_path = str(Path(str(self.temp_dir.name)) / self.filename)
        async with aiofiles.open(file_path, 'wb') as file_for_writing:
            async for chunk in content_generator:
                await file_for_writing.write(chunk)
        return file_path

    async def extract_files(
        self: 'FileRepositoryV1',
        path_to_file: str,
    ) -> str:
        """Extract archive in thread pool and return path."""
        await self.activate_temp_dir()
        executor = ThreadPoolSingleton().thread_pool
        loop = asyncio.get_running_loop()
        future = loop.run_in_executor(
            executor,
            self._sync_extract_files,
            path_to_file,
        )
        return await future

    def _sync_extract_files(
        self: 'FileRepositoryV1',
        path_to_file: str,
    ) -> str:
        """Extract archive to its dir."""
        path_to_dir = Path(path_to_file).parent
        with ZipFile(
            path_to_file,
            'r',
        ) as zip_ref:
            zip_ref.extractall(path_to_dir)
        return str(path_to_dir)
