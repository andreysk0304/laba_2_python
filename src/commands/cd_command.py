import logging
import os

from src.utils.tokenizer import tokenizer

from src.components.shell import Shell
from src.decorators.register_command import register_command


@register_command('cd', 'cd <path> - перейти в директорию | cd - перейти в корневую директорию.')
def cd_func(command: str) -> None:

    tokens = tokenizer(command)

    if len(tokens) == 0:
        cd_clear_func()

        return

    elif len(tokens) > 1:
        logging.error(f"to many params.")

        print(f"to many params.")

        return

    path = tokens[0]

    new_path = Shell.resolve_path(path)

    if not os.path.isdir(new_path):
        logging.error(f"catalog '{new_path}' not found.")

        print(f"catalog '{new_path}' not found.")

        return

    Shell.current_path = new_path

    return


def cd_clear_func() -> None:
    Shell.cler_path()

    return