import logging
import os

from src.utils.messages import log_print
from src.utils.tokenizer import tokenizer

from src.components.shell import Shell
from src.components.command import Command

from src.decorators.register_command import register_command


@register_command('cd', 'cd <path> - перейти в директорию | cd - перейти в корневую директорию.')
def cd_func(command: Command) -> None:
    if len(command.paths) == 0:
        cd_clear_func()
        return

    elif len(command.paths) > 1:
        log_print('to many params')
        return

    path = command.paths[0]

    new_path = Shell.resolve_path(path)

    if not os.path.isdir(new_path):
        log_print(f"catalog '{new_path}' not found.")
        return

    Shell.current_path = new_path
    return


def cd_clear_func() -> None:
    Shell.cler_path()
    return