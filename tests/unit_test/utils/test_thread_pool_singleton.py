"""Testing thread pool."""
from concurrent.futures import ThreadPoolExecutor

from src.utils.thread_pool_singleton import ThreadPoolSingleton


class TestThreadPoolSingleton(object):
    """Tests for ThreadPoolSingleton."""

    def test_singleton(
        self: 'TestThreadPoolSingleton',
    ):
        """Test is singleton."""
        thread_pool = ThreadPoolSingleton()
        other_thread_pool = ThreadPoolSingleton()
        assert thread_pool == other_thread_pool

    def test_thread_pool(
        self: 'TestThreadPoolSingleton',
    ):
        """Test providing thread pool."""
        thread_pool = ThreadPoolSingleton()
        assert isinstance(thread_pool.thread_pool, ThreadPoolExecutor)
