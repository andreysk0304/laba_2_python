from src.decorators.register_command import register_command
from src.components.shell import Shell
from src.utils.messages import log_print

@register_command('undo', 'Команда undo отменит последнее действие команд (rm, mv, cp).')
def undo_func(command: str = None) -> None:

    try:
        Shell.move_file_directory_from_trash()

        print('last move has been canceled.')

    except Exception as error:
        log_print(f'{error}')