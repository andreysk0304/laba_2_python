from src.decorators.register_command import register_command

from src.components.shell import Shell
from src.components.command import Command

from src.utils.messages import log_print


@register_command('undo', 'Команда undo отменит последнее действие команд (rm, mv, cp).')
def undo_func(command: Command) -> None:

    last_command = Shell.get_last_operation_name()

    if last_command == 'rm':
        try:
            Shell.move_file_directory_from_trash()
        except Exception as error:
            log_print(f'{error}')
            return

    elif last_command == 'cp':
        try:
            Shell.remove_copied_file_or_directory()
        except Exception as error:
            log_print(f'{error}')
            return

    elif last_command == 'mv':
        try:
            Shell.move_file_or_directory_back()
        except Exception as error:
            log_print(f'{error}')
            return

    else:
        return

    print('last move has been canceled.')