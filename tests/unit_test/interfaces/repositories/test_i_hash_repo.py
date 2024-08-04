"""Tests for interface hash repo."""
from src.interfaces.repositories.i_hash_repo import IHashRepository


class TestIHashRepository(object):
    """Testing methods and fields."""

    def test_get_filenames_with_hashes_method(
        self: 'TestIHashRepository',
    ):
        """Testing get_filenames_with_hashes method existing."""
        assert IHashRepository.get_filenames_with_hashes
