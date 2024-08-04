"""Tests for file-metadata type."""
from src.domain.file_metadata import FileMetadata


class TestFileMetadata(object):
    """Testing fields and validation."""

    def test_filename_field(
        self: 'TestFileMetadata',
    ):
        """Testing filename field existing."""
        assert 'filename' in FileMetadata.__annotations__

    def test_hash_field(
        self: 'TestFileMetadata',
    ):
        """Testing hash field existing."""
        assert 'hash' in FileMetadata.__annotations__
