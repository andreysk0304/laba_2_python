import os

from src.decorators.register_command import register_command
from src.exceptions.exceptions import InvalidArgumentsCount, CodeError, DirectoryNotFound
from src.utils.loggers import console_logger

from src.components.shell import Shell
from src.components.command import Command


@register_command('mv', 'Команда mv <from_path> <to_path> перемещает файл/директорию из <from_path> в <to_path>')
def mv_func(command: Command) -> None:
    '''
    Функция перемещает файл / директорию из <from_path> в <to_path>

    :param command: Команда из консоли
    :return: Ничего
    '''

    if len(command.paths) != 2:
        raise InvalidArgumentsCount(command.command)

    from_path, to_path = command.paths[0], command.paths[1]

    if not os.path.exists(from_path):
        raise DirectoryNotFound(from_path)

    dest_dir = os.path.dirname(to_path) or '.'

    if dest_dir and not os.path.exists(dest_dir):
        raise DirectoryNotFound(dest_dir)

    try:
        Shell.move_file_or_directory(to_path=to_path, from_path=from_path)
        console_logger.info('Объект успешно перемещён.')
    except Exception as error:
        raise CodeError(f'{error}')