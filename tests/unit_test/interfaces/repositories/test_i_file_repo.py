"""Tests for interface file repo."""
from src.interfaces.repositories.i_file_repo import IFileRepository


class TestIFileRepository(object):
    """Testing methods and fields."""

    def test_write_file_method(
        self: 'TestIFileRepository',
    ):
        """Testing write_file method existing."""
        assert IFileRepository.write_file

    def test_extract_files_method(
        self: 'TestIFileRepository',
    ):
        """Testing extract_files method existing."""
        assert IFileRepository.extract_files
