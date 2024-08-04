"""Module with file entity."""

from pydantic import BaseModel


class FileMetadata(BaseModel):
    """Realization of file entity."""

    filename: str
    hash: str
