import logging
import os

from src.exceptions.exceptions import InvalidArgumentsCount, CatalogNotFound

from src.components.shell import Shell
from src.components.command import Command

from src.decorators.register_command import register_command


@register_command('cd', 'cd <path> - перейти в директорию | cd - перейти в корневую директорию.')
def cd_func(command: Command) -> None:
    '''
    Команда переходит в указанную директорию, поддерживает, как абсолютный, так и относительный путь.

    :param command: Команда из консоли
    :return: Переход по указанному пути (меняется current_path в классе shell)
    '''


    if len(command.paths) == 0:
        cd_clear_func()
        return

    elif len(command.paths) > 1:
        raise InvalidArgumentsCount(command.command)

    path = command.paths[0]

    new_path = Shell.resolve_path(path)

    if not os.path.isdir(new_path):
        raise CatalogNotFound(new_path)

    Shell.current_path = new_path

    return


def cd_clear_func() -> None:
    '''
    Функция сбрасывает текущий путь в самое начало до C://

    :return: Ничего
    '''

    Shell.cler_path()

    return