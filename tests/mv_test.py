import pytest
from pyfakefs.fake_filesystem import FakeFilesystem

from unittest.mock import Mock

from src.components.shell import Shell

from src.commands.mv_command import mv_func
from src.commands.ls_command import ls_func
from src.components.command import Command
from src.exceptions.exceptions import DirectoryNotFound, InvalidArgumentsCount


def test_mv_func(fs: FakeFilesystem, fake_console_logger: Mock):
    fs.create_file('test')
    fs.create_dir('moved')

    Shell.undo_path = '/.undo'
    mv_func(Command('mv test moved'))

    ls_func(Command('ls moved'))
    output_moved = fake_console_logger.call_args.args[0]

    ls_func(Command('ls'))
    output = fake_console_logger.call_args.args[0]

    assert 'test' in output_moved and 'test' not in output


def test_mv_invalid_argument_count_func():
    with pytest.raises(InvalidArgumentsCount):
        mv_func(Command('mv test teste tefjdkbnfdjk fjdbnfhjkdbfd jfdbjkhfdgjhfdv'))


def test_mv_file_or_directory_not_found():
    with pytest.raises(DirectoryNotFound):
        mv_func(Command('mv test test'))

    with pytest.raises(DirectoryNotFound):
        mv_func(Command('mv kfdnfd test'))