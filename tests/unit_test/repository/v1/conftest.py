"""Conftest for v1 repository."""
import io
import zipfile
from tempfile import TemporaryDirectory
from typing import Any, AsyncGenerator

import pytest
import pytest_asyncio


@pytest_asyncio.fixture()
async def async_archive_generator_fixture():
    return byte_generator()


async def byte_generator() -> AsyncGenerator[bytes, Any]:
    buffer = io.BytesIO()

    with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        zip_file.writestr(
            'example.txt',
            'This is a test file inside the ZIP archive.',
        )

    while True:
        chunk = buffer.read(1024)
        if not chunk:
            break
        yield chunk


@pytest.fixture()
def temp_archive_fixture():
    with TemporaryDirectory() as temp_dir:
        zip_path = '{0}/mock_files.zip'.format(temp_dir)

        with io.BytesIO() as buffer:
            with zipfile.ZipFile(
                buffer,
                'w',
                zipfile.ZIP_DEFLATED,
            ) as zip_file:
                zip_file.writestr(
                    'file1.txt',
                    'This is the content of file 1.',
                )
                zip_file.writestr(
                    'file2.txt',
                    'This is the content of file 2.',
                )

            with open(zip_path, 'wb') as archive:
                archive.write(buffer.getvalue())

        yield zip_path
