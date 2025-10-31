import os

from src.decorators.register_command import register_command
from src.utils.messages import log_print
from src.utils.tokenizer import tokenizer

from src.components.shell import Shell
from src.components.command import Command


@register_command('mv', 'Команда mv <from_path> <to_path> перемещает файл/директорию из <from_path> в <to_path>')
def cp_func(command: Command) -> None:
    if len(command.paths) != 2:
        log_print('Params count error.')
        return

    from_path, to_path = command.paths[0], command.paths[1]

    try:
        Shell.move_file_or_directory(to_path=to_path, from_path=from_path)
        print('Object moved successful')
    except Exception as error:
        log_print(f'{error}')