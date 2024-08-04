"""Testing dependencies for v1 controller."""

from src.controllers.v1.dependencies import (
    FileRepositoryType,
    HashRepositoryType,
    HttpRepositoryType,
)
from src.interfaces.repositories.i_file_repo import IFileRepository
from src.interfaces.repositories.i_hash_repo import IHashRepository
from src.interfaces.repositories.i_http_repo import IHttpRepository


def test_file_repository_type():
    assert issubclass(FileRepositoryType, IFileRepository)


def test_hash_repository_type():
    assert issubclass(HashRepositoryType, IHashRepository)


def test_http_repository_type():
    assert issubclass(HttpRepositoryType, IHttpRepository)
