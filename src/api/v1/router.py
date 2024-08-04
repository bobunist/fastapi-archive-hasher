"""Module with v1 router."""
from typing import List

from fastapi import APIRouter

from src.api.v1.dependencies import DownloadArchiveControllerV1Dep
from src.config import Settings
from src.domain.file_metadata import FileMetadata

router = APIRouter(
    tags=['main_router'],
    prefix='/v1',
)


@router.get('/download', response_model_exclude_defaults=True)
async def download_archive_v1(
    download_repo_controller: DownloadArchiveControllerV1Dep,
) -> List[FileMetadata]:
    """Endpoint for triple downloading repository and hashing files."""
    return await download_repo_controller.execute(
        Settings().repo_url,
    )
