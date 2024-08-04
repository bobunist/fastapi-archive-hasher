"""Module with http repo interface."""

from abc import ABC, abstractmethod
from typing import AsyncGenerator


class IHttpRepository(ABC):
    """Interface for http repo."""

    @abstractmethod
    async def fetch(
        self: 'IHttpRepository',
        url: str,
    ) -> AsyncGenerator[bytes, None]:
        """Download data by chunks."""
        yield  # pragma: no cover
        raise NotImplementedError
