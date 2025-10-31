from src.decorators.register_command import register_command
from src.exceptions.exceptions import InvalidArgumentsCount, CodeError
from src.utils.loggers import console_logger

from src.components.shell import Shell
from src.components.command import Command


@register_command('cp', 'Команда cp <from_path> <to_path> копирует файл из <from_path> в <to_path>')
def cp_func(command: Command) -> None:
    '''
    Команда cp копирует указзаный файл из одной директории в другую ( из <from_path> в <to_path>.

    :param command: Команда из консоли
    :return: Ничего
    '''

    if len(command.paths) != 2:
        raise InvalidArgumentsCount(command.command)

    from_path, to_path = command.paths[0], command.paths[1]

    try:
        Shell.copy_file_or_directory(to_path=to_path, from_path=from_path)
        console_logger.info('Копия успешно создана!')

    except Exception as error:
        raise CodeError(f'{error}')