import logging
import os
from pathlib import Path

from src.utils.messages import log_print
from src.utils.tokenizer import tokenizer

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
        log_print('to many params.')

        return

    filename = command.paths[0]

    file_path = Shell.resolve_path(filename)

    if not os.path.exists(file_path):
        log_print(f"file '{file_path}' not found.")
        return

    if os.path.isdir(file_path):
        log_print(f"Error: '{file_path}', '{filename}' - is catalog.")
        return

    try:
        print(f'filename: {filename}\n{"-" * 50}')

        path = Path(file_path)

        try:
            print(path.read_text(encoding="utf-8"))
        except UnicodeDecodeError:
            print(path.read_text(encoding='iso-8859-1'))


    except PermissionError:
        log_print(f"You not have permissions for '{file_path}'")
    except UnicodeDecodeError:
        log_print(f"'{file_path}' is not text file.")