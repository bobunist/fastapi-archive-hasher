"""Module with fetch file use case."""
from typing import AsyncGenerator

from src.interfaces.repositories.i_http_repo import IHttpRepository


class FetchFileUseCase(object):
    """Download file use case."""

    def __init__(
        self: 'FetchFileUseCase',
        network_repo: IHttpRepository,
    ) -> None:
        """Define repos for use cases."""
        self.network_repo = network_repo

    async def execute(
        self: 'FetchFileUseCase',
        url: str,
    ) -> AsyncGenerator[bytes, None]:
        """Get generator from http request with file."""
        return self.network_repo.fetch(url)
