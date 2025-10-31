from unittest.mock import Mock

from pyfakefs.fake_filesystem import FakeFilesystem

from src.commands.zip_command import zip_func
from src.commands.ls_command import ls_func

from src.components.command import Command


def test_zip_func(fs: FakeFilesystem, fake_console_logger: Mock):

    fs.create_dir('test_create_dir')

    zip_func(Command('zip test_create_dir test_create_dir.zip'))
    ls_func(Command('ls'))
    output = fake_console_logger.call_args.args[0]

    assert 'test_create_dir.zip' in output