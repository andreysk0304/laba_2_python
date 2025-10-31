from src.decorators.register_command import register_command

from src.components.shell import Shell
from src.components.command import Command
from src.exceptions.exceptions import CodeError


@register_command('undo', 'Команда undo отменит последнее действие команд (rm, mv, cp).')
def undo_func(command: Command) -> None:

    '''
    Функция отменяет действие последней использованной команды

    rm - возвращаем файл из .trash
    cp - удаляет копию
    mv - возвращаем обратно файл туда откуда изначально мувнули
    :param command: Команда из консоли
    :return: Ничего
    '''

    last_command = Shell.get_last_operation_name()

    if last_command == 'rm':
        try:
            Shell.move_file_directory_from_trash()
        except Exception as error:
            raise CodeError(f'{error}')

    elif last_command == 'cp':
        try:
            Shell.remove_copied_file_or_directory()
        except Exception as error:
            raise CodeError(f'{error}')

    elif last_command == 'mv':
        try:
            Shell.move_file_or_directory_back()
        except Exception as error:
            raise CodeError(f'{error}')

    else:
        return

    print('last move has been canceled.')