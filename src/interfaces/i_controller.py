"""Module with controller base class."""

from abc import ABC, abstractmethod
from typing import Any, Dict, Tuple


class IController(ABC):
    """Controller base class."""

    @abstractmethod
    async def execute(
        self: 'IController',
        *args: Tuple[Any, ...],
        **kwargs: Dict[str, Any],
    ) -> Tuple[Any, ...]:
        """Execute controller."""
        raise NotImplementedError
