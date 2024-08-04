"""Module with thread pool for async using."""

from concurrent.futures import ThreadPoolExecutor

from singleton import Singleton


class ThreadPoolSingleton(object, metaclass=Singleton):
    """Thread pool for async using."""

    _instance = None

    def __init__(
        self: 'ThreadPoolSingleton',
    ) -> None:
        """Assign thread pool to singleton."""
        self.thread_pool = ThreadPoolExecutor()
