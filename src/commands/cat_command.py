import os
from pathlib import Path

from src.exceptions.exceptions import InvalidArgumentsCount, FileNotFound, IsDirectory, NotEnoughPermissions, IsNotTextFile
from src.utils.loggers import console_logger

from src.components.shell import Shell
from src.components.command import Command
from src.decorators.register_command import register_command


@register_command('cat', 'Команда cat <path> выводит содержимое указанного файла.')
def cat_func(command: Command) -> None:
    '''
    Функция выводит содержимое файла.

    :param command: Команда из консоли.
    :return: Содержимое файла.
    '''

    if len(command.paths) > 1:
        raise InvalidArgumentsCount(command.command)

    filename = command.paths[0]

    file_path = Shell.resolve_path(filename)

    if not os.path.exists(file_path):
        raise FileNotFound(file_path)

    if os.path.isdir(file_path):
        raise IsDirectory(file_path)

    try:
        console_logger.info(f'filename: {filename}\n{"-" * 50}')

        path = Path(file_path)

        try:
            console_logger.info(path.read_text(encoding="utf-8"))
        except UnicodeDecodeError:
            console_logger.info(path.read_text(encoding='iso-8859-1'))


    except PermissionError:
        raise NotEnoughPermissions()
    except UnicodeDecodeError:
        raise IsNotTextFile()