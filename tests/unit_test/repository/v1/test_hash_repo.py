"""Testing hash repo v1."""
import pytest

from src.domain.file_metadata import FileMetadata
from src.repository.v1.hash_repo import HashRepositoryV1


class TestHashRepository(object):
    """Tests for HashRepositoryV1."""

    @pytest.mark.asyncio()
    async def test_get_filenames_with_hashes(
        self: 'TestHashRepository',
    ):
        """Test get files metadata from dir."""
        files_metadata = await HashRepositoryV1().get_filenames_with_hashes(
            '.',
        )
        assert isinstance(files_metadata, list)
        for metadata in files_metadata:
            assert isinstance(metadata, FileMetadata)
