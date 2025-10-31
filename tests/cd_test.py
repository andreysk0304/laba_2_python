import pytest
from pyfakefs.fake_filesystem import FakeFilesystem

from src.components.shell import Shell

from src.commands.cd_command import cd_func
from src.components.command import Command
from src.exceptions.exceptions import CatalogNotFound, InvalidArgumentsCount


def test_cd_func(fs: FakeFilesystem):
    fs.create_dir('test')

    cd_func(Command("cd test"))
    assert Shell.current_path == 'C:\\test'

    cd_func(Command("cd ."))
    assert Shell.current_path == 'C:\\test'

    cd_func(Command("cd .."))
    assert Shell.current_path == 'C:\\'

    cd_func(Command("cd"))
    assert Shell.current_path == 'C:\\'


def test_cd_invalid_path_func(fs: FakeFilesystem):
    fs.create_dir('test')

    with pytest.raises(CatalogNotFound):
        cd_func(Command("cd cringe_kakoyto"))


def test_cd_invalid_count_func(fs: FakeFilesystem):
    fs.create_dir('test')

    with pytest.raises(InvalidArgumentsCount):
        cd_func(Command("cd . . . fd fd fd"))

    with pytest.raises(InvalidArgumentsCount):
        cd_func(Command("cd why hello hello"))

    with pytest.raises(InvalidArgumentsCount):
        cd_func(Command("cd mg mg"))