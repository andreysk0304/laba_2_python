from unittest.mock import Mock

from pyfakefs.fake_filesystem import FakeFilesystem

from src.commands.zip_command import zip_func, unzip_func
from src.commands.ls_command import ls_func

from src.components.command import Command


def test_unzip_func(fs: FakeFilesystem, fake_console_logger: Mock):

    fs.create_dir('test_create_dir')
    fs.create_dir('unzipped')

    zip_func(Command('zip test_create_dir test_create_dir.zip'))
    unzip_func(Command('unzip test_create_dir.zip unzipped'))
    ls_func(Command('ls unzipped'))
    output = fake_console_logger.call_args.args[0]

    assert 'unzipped' in output