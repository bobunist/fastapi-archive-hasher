"""Module with http repo."""
from typing import AsyncGenerator

import aiohttp

from src.interfaces.repositories.i_http_repo import IHttpRepository


class HttpRepositoryV1(IHttpRepository):
    """Http repo implementation."""

    async def fetch(
        self: 'HttpRepositoryV1',
        url: str,
    ) -> AsyncGenerator[bytes, None]:
        """Fetch data by http."""
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                async for chunk in response.content.iter_chunked(1024):
                    yield chunk
