import pytest
from pyfakefs.fake_filesystem import FakeFilesystem

from unittest.mock import Mock

from src.components.shell import Shell

from src.commands.cp_command import cp_func
from src.commands.ls_command import ls_func
from src.components.command import Command
from src.exceptions.exceptions import DirectoryNotFound, InvalidArgumentsCount


def test_cp_func(fs: FakeFilesystem, fake_console_logger: Mock):
    fs.create_file('test')
    fs.create_dir('copy')

    Shell.undo_path = '/.undo'
    cp_func(Command('cp test copy'))
    ls_func(Command('ls copy'))

    output = fake_console_logger.call_args.args[0]

    assert 'test' in output


def test_cp_file_not_found_func():
    Shell.undo_path = '/.undo'

    with pytest.raises(DirectoryNotFound):
        cp_func(Command('cp test test1'))


def test_cp_argument_count_func():
    Shell.undo_path = '/.undo'

    with pytest.raises(InvalidArgumentsCount):
        cp_func(Command('cp kfd fkdn fdjn fjdnfd'))