"""Dependencies for v1 controllers."""
from src.repository.v1.file_repo import FileRepositoryV1
from src.repository.v1.hash_repo import HashRepositoryV1
from src.repository.v1.http_repo import HttpRepositoryV1

FileRepositoryType = FileRepositoryV1
HashRepositoryType = HashRepositoryV1
HttpRepositoryType = HttpRepositoryV1
