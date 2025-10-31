import pytest
from pyfakefs.fake_filesystem import FakeFilesystem

from unittest.mock import Mock

from src.commands.cd_command import cd_func
from src.commands.history_command import history_func
from src.components.shell import Shell

from src.commands.mv_command import mv_func
from src.commands.ls_command import ls_func
from src.components.command import Command
from src.exceptions.exceptions import DirectoryNotFound, InvalidArgumentsCount
from src.main import use_command


def test_history_func(fs: FakeFilesystem, fake_console_logger: Mock):
    fs.create_file('test')
    fs.create_dir('moved')

    Shell.history_path = '/.history'
    use_command('ls -l')
    use_command('cd moved')
    use_command('history')

    output = fake_console_logger.call_args.args[0]

    assert '1. history' in output and '2. cd moved' in output and '3. ls -l' in output


def test_history_with_count_func(fs: FakeFilesystem, fake_console_logger: Mock):
    fs.create_file('test')
    fs.create_dir('moved')

    Shell.history_path = '/.history'
    use_command('ls -l')
    use_command('cd moved')
    use_command('history 1')

    output = fake_console_logger.call_args.args[0]

    assert '1. history' in output and '2. cd moved' not in output and '3. ls -l' not in output