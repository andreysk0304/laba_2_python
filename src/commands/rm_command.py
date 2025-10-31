from src.exceptions.exceptions import InvalidArgumentsCount, CannotRemove, CannotRemoveNotFound, CodeError
from src.utils.loggers import console_logger

from src.decorators.register_command import register_command

from src.components.command import Command
from src.components.shell import Shell

from pathlib import Path


@register_command('rm', 'Команда rm <path> удаляет указанный файл.')
def rm_func(command: Command, is_test: bool = False) -> None:
    '''
    Функция удаляет файл/директорию <path> (по факту перемещает в .trash)

    :param command: Команда из консоли
    :return: Ничего
    '''

    recursive: bool = False # Включено ли рекурсивное удаление

    if '-r' in command.flags:
        recursive = True

    if len(command.paths) != 1:
        raise InvalidArgumentsCount(command.command)

    target = Shell.resolve_path(command.paths[0])

    path = Path(target)

    if path.resolve() == Path('/').resolve():
        raise CannotRemove('/')

    if path.resolve() == Path('..').resolve() or path.name == '..':
        raise CannotRemove('..')

    if path.resolve() == Path('.').resolve() or path.name == '.':
        raise CannotRemove('.')

    if not path.exists():
        raise CannotRemoveNotFound(f'{path}')

    try:
        if not is_test:
            check: str = input('You are agree ? [y/n\n')

        else:
            check: str = 'y'

        if check.strip().lower() == 'y':
            Shell.move_file_directory_to_trash(target, recursive)
            console_logger.info(f"'{path}' успешно удалён!")
            return

        else:
            console_logger.info(f'{path} удаление прервано!')
            return

    except Exception as error:
        raise CodeError(f'{error}')