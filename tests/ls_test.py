import os
import pytest

from pyfakefs.fake_filesystem import FakeFilesystem

from unittest.mock import Mock

from src.commands.ls_command import ls_func

from src.components.command import Command
from src.exceptions.exceptions import NotEnoughPermissions, FileNotFound


def test_ls_func(fs: FakeFilesystem, fake_console_logger: Mock):
    fs.create_dir("test")
    fs.create_file(os.path.join("test", "hello tester.txt"), contents="hello tester")
    fs.create_file("100plz.txt", contents="Поставьте максимум пожалуйста :D")

    ls_func(Command('ls'))
    output = fake_console_logger.call_args.args[0]

    assert 'test' in output and '100plz.txt' in output


def test_ls_l_func(fs: FakeFilesystem, fake_console_logger: Mock):
    fs.create_dir("test")
    fs.create_file(os.path.join("test", "hello tester.txt"), contents="hello tester")
    fs.create_file("можно100пж.txt", contents="Поставьте максимум пожалуйста :D")

    ls_func(Command('ls test -l'))
    output = fake_console_logger.call_args.args[0]

    assert 'hello tester.txt' in output and 'rw-rw-rw-' in output


def test_is_not_directory_func(fs: FakeFilesystem, fake_full_logger: Mock):
    fs.create_file('text.txt')

    ls_func(Command('ls text.txt'))
    output = fake_full_logger.call_args.args[0]

    assert 'не является директорией' in output