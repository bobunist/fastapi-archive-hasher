"""Tests for interface http repo."""
from src.interfaces.repositories.i_http_repo import IHttpRepository


class TestIHttpRepository(object):
    """Testing methods and fields."""

    def test_fetch_method(
        self: 'TestIHttpRepository',
    ):
        """Testing fetch method existing."""
        assert IHttpRepository.fetch
