"""Module with dependencies for app."""
from typing import Annotated

from fastapi import Depends

from src.controllers.v1.download_archive_controller import (
    DownloadArchiveControllerV1,
)
from src.interfaces.i_controller import IController


def provide_download_archive_controller_v1() -> DownloadArchiveControllerV1:
    """Provide controller for endpoint param dependency."""
    return DownloadArchiveControllerV1()


DownloadArchiveControllerV1Dep = Annotated[
    IController,
    Depends(
        provide_download_archive_controller_v1,
        use_cache=False,
    ),
]
