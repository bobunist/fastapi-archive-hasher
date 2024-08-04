"""Tests for interface controller."""
from src.interfaces.i_controller import IController


class TestIController(object):
    """Testing methods and fields."""

    def test_get_filenames_with_hashes_method(
        self: 'TestIController',
    ):
        """Testing execute method existing."""
        assert IController.execute
