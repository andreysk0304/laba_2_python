from pyfakefs.fake_filesystem import FakeFilesystem

from unittest.mock import Mock

from src.commands.undo_command import undo_func
from src.components.shell import Shell

from src.commands.rm_command import rm_func
from src.commands.ls_command import ls_func
from src.components.command import Command


def test_undo_func(fs: FakeFilesystem, fake_console_logger: Mock):
    fs.clear_cache()

    fs.create_file('проверка_ундо_1')
    fs.create_file('проверка_ундо_2')

    Shell.undo_path = '/.undo'
    Shell._ensure_undo_json()

    Shell.trash_path = '/.trash'
    Shell._ensure_trash_dir()

    rm_func(Command('rm проверка_ундо_1'), is_test=True)
    rm_func(Command('rm проверка_ундо_2'), is_test=True)
    ls_func(Command('ls'))
    output_removed = fake_console_logger.call_args.args[0]

    undo_func(Command('undo'))
    undo_func(Command('undo'))
    ls_func(Command('ls'))

    output = fake_console_logger.call_args.args[0]

    assert 'проверка_ундо' not in output_removed and 'проверка_ундо_1' in output and 'проверка_ундо_2' in output
