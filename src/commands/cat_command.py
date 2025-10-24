import logging
import os

from src.utils.tokenizer import tokenizer

from src.components.shell import Shell
from src.decorators.register_command import register_command


@register_command('cat', 'Команда cat <path> выводит содержимое указанного файла.')
def cat_func(command: str) -> None:
    '''
    Функция выводит содержимое файла.

    :param command: Команда из консоли.
    :return: Содержимое файла.
    '''

    tokens = tokenizer(command)

    if len(tokens) > 1:
        logging.error('to many params.')

        print('to many params.')

        return

    filename = tokens[0]

    file_path = Shell.resolve_path(filename)

    if not os.path.exists(file_path):
        logging.error(f"file '{file_path}' not found.")

        print(f"Error: file '{file_path}' not found.")

        return

    if os.path.isdir(file_path):
        logging.error(f"{file_path}', '{filename}' - is catalog.")

        print(f"Error: '{file_path}', '{filename}' - is catalog.")

        return

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        print(f'filename: {filename}\n{"-" * 50}')
        print(content)

    except PermissionError:
        logging.error(f"you not have permissions for {file_path}'.")

        print(f"Error: you not have permissions for {file_path}'.")

    except UnicodeDecodeError:
        logging.error(f"'{file_path}' is not text file.")

        print(f"Error: '{file_path}' is not text file.")