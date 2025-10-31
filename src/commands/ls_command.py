import os
import logging
import stat
import datetime

from src.components.shell import Shell
from src.components.command import Command

from src.decorators.register_command import register_command
from src.exceptions.exceptions import FileNotFound, NotEnoughPermissions
from src.utils.loggers import console_logger


@register_command('ls', 'Выводит в консоль всё содержимое текущей директории. Флаг -l позволяет увидеть расширенную информацию, пример ввода: ls -l')
def ls_func(command: Command) -> None:
    '''
    Функция выводит содержимое текущей директории (Shell.current_path) или указанной директории в ls <path>

    Флаг -l выводит дополнительную информациб о файлах

    :param command: Команда из консоли
    :return: Содержимое директории / директорий
    '''

    long: bool = False # включён ли флаг -l

    if '-l' in command.flags:
        long = True

    paths = command.paths

    if not paths:
        paths.append(' ')

    for path in paths:
        if path == '' or path == ' ':
            path = '.'
        target = Shell.resolve_path(path)
        try:
            files = os.listdir(target)
        except FileNotFoundError:
            raise FileNotFound(path)
        except PermissionError:
            raise NotEnoughPermissions()

        if not long:
            console_logger.info(f'\n>{path}')
            for file in files:
                console_logger.info(file)
            console_logger.info("-" * 50)
        else:
            console_logger.info(f'\n>{path}')
            console_logger.info(f"{'MODE':<11} {'SIZE':>10} {'LAST MODIFIED':<17} NAME")
            console_logger.info("-" * 50)

            for file in files:
                full = os.path.join(target, file)
                st = os.stat(full)
                mode = stat.filemode(st.st_mode)
                size = st.st_size
                mtime = datetime.datetime.fromtimestamp(st.st_mtime).strftime('%Y-%m-%d %H:%M')

                console_logger.info(f"{mode} {size:>10} {mtime} {file}")

            console_logger.info("-" * 50)