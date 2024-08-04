"""Module with hash repo."""
import hashlib
from pathlib import Path
from typing import List

import aiofiles

from src.domain.file_metadata import FileMetadata
from src.interfaces.repositories.i_hash_repo import IHashRepository


class HashRepositoryV1(IHashRepository):
    """Hash repo implementation."""

    async def get_filenames_with_hashes(
        self: 'HashRepositoryV1',
        root_dir: str,
    ) -> List[FileMetadata]:
        """Walk by every file in dir and returns file metadata."""
        file_hashes = []
        path = Path(root_dir)
        for entry in path.rglob('*'):
            if entry.is_file():
                file_hash = await self._calculate_hash(str(entry))
                file_hashes.append(
                    FileMetadata(
                        filename=str(entry.relative_to(path)),
                        hash=file_hash,
                    ),
                )
        return file_hashes

    async def _calculate_hash(
        self: 'HashRepositoryV1',
        file_path: str,
    ) -> str:
        """Calculate hash of file."""
        sha256_hash = hashlib.sha256()
        async with aiofiles.open(file_path, 'rb') as file_for_hashing:
            chunk = await file_for_hashing.read(1024)
            while chunk:
                sha256_hash.update(chunk)
                chunk = await file_for_hashing.read(1024)
        return sha256_hash.hexdigest()
