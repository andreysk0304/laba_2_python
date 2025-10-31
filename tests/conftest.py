import pytest

from unittest.mock import Mock
from pytest_mock import MockerFixture


@pytest.fixture
def fake_console_logger(mocker: MockerFixture) -> Mock:
    mock_console_logger = mocker.patch("src.utils.loggers.console_logger.info")

    return mock_console_logger


@pytest.fixture
def fake_full_logger(mocker: MockerFixture) -> Mock:
    mock_full_logger = mocker.patch("src.utils.loggers.full_logger.error")

    return mock_full_logger

'''
@pytest.fixture
def fake_project_dir(monkeypatch):
    monkeypatch.setattr(src., "UNDO_HISTORY_FILE", "/.undo_history.jsonl")
'''