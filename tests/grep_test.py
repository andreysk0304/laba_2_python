import pytest
from pyfakefs.fake_filesystem import FakeFilesystem

from unittest.mock import Mock

from src.commands.grep_command import grep_func
from src.components.command import Command

from src.exceptions.exceptions import InvalidArgumentsCount


def test_cp_func(fs: FakeFilesystem, fake_console_logger: Mock):
    fs.create_file('test', contents="привет\nя люблю эту прогу\n\nочень сильно, правдааа! :)))\n\nпривет снова\n\nи снова привет!".encode('utf-8'))

    grep_func(Command('grep привет test'))

    output = fake_console_logger.call_args.args[0]

    assert 'привет' in output


def test_grep_invalid_argument_count():
    with pytest.raises(InvalidArgumentsCount):
        grep_func(Command('grep fkdnfdjk kjdfbkhfdb jhfbdjhfdb hfdbghjfdb hfjdbghfkdb'))


def test_rec_func(fs: FakeFilesystem, fake_console_logger: Mock):
    fs.create_dir('test')
    fs.create_file('test/test', contents='test\n\n\ntest\n\nnetest jfdbjdf\nfdjbfd')

    grep_func(Command('grep test test -r'))

    output = fake_console_logger.call_args.args[0]

    assert 'test' in output

