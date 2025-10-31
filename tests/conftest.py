import pytest

from unittest.mock import Mock

from pyfakefs.fake_filesystem import FakeFilesystem
from pytest_mock import MockerFixture

from src.components.shell import Shell


@pytest.fixture
def fake_console_logger(mocker: MockerFixture) -> Mock:
    mock_console_logger = mocker.patch("src.utils.loggers.console_logger.info")

    return mock_console_logger


@pytest.fixture
def fake_full_logger(mocker: MockerFixture) -> Mock:
    mock_full_logger = mocker.patch("src.utils.loggers.full_logger.error")

    return mock_full_logger


@pytest.fixture(autouse=True)
def change_dir(fs: FakeFilesystem):
    Shell.current_path = '/'