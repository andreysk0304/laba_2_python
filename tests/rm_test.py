import pytest
from pyfakefs.fake_filesystem import FakeFilesystem

from unittest.mock import Mock

from src.components.shell import Shell

from src.commands.rm_command import rm_func
from src.commands.ls_command import ls_func
from src.components.command import Command
from src.exceptions.exceptions import InvalidArgumentsCount, CannotRemove


def test_rm_func(fs: FakeFilesystem, fake_console_logger: Mock):
    fs.create_file('проверка_рм')

    Shell.undo_path = '/.undo'

    Shell.trash_path = '/.trash'
    Shell._ensure_trash_dir()

    rm_func(Command('rm проверка_рм'), is_test=True)
    ls_func(Command('ls'))

    output = fake_console_logger.call_args.args[0]

    assert 'проверка_рм' not in output


def test_rm_arguments_count_func():
    with pytest.raises(InvalidArgumentsCount):
        rm_func(Command('rm fdjnfjd fjdnfjd'))


def test_rm_cannot_remove_func():

    with pytest.raises(CannotRemove):
        rm_func(Command('rm .'))

    with pytest.raises(CannotRemove):
        rm_func(Command('rm /'))

    with pytest.raises(CannotRemove):
        rm_func(Command('rm ..'))