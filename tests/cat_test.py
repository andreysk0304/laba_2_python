import pytest
from pyfakefs.fake_filesystem import FakeFilesystem

from unittest.mock import Mock

from src.commands.cat_command import cat_func
from src.components.command import Command
from src.exceptions.exceptions import IsDirectory, FileNotFound


def test_cat_func(fs: FakeFilesystem, fake_console_logger: Mock):
    fs.create_file('test file', contents='test')

    cat_func(Command('cat "test file"'))
    output = fake_console_logger.call_args.args[0]

    assert output == 'test'


def test_cat_invalid_path_func():
    with pytest.raises(FileNotFound):
        cat_func(Command("cat скучно"))


def test_cat_is_dir_func(fs: FakeFilesystem):
    fs.create_dir('test')
    with pytest.raises(IsDirectory):
        cat_func(Command('cat test'))