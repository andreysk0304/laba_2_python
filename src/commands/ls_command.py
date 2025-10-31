import os
import logging
import stat
import datetime

from src.components.shell import Shell
from src.components.command import Command

from src.decorators.register_command import register_command
from src.exceptions.exceptions import FileNotFound, NotEnoughPermissions
from src.utils.loggers import console_logger, full_logger


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

        if not os.path.isdir(target):
            full_logger.error(f"'{path}' не является директорией")
            continue

        try:
            files = os.listdir(target)
        except FileNotFoundError:
            raise FileNotFound(path)
        except PermissionError:
            raise NotEnoughPermissions()

        msg: str = ''

        if not long:
            msg += f'{path}\n'

            for file in files:
                msg += file+'\n'

            msg += "-" * 50

            console_logger.info(msg)
        else:

            msg += f'{path}\n'
            msg += f"{'MODE':<11} {'SIZE':>10} {'LAST MODIFIED':<17} NAME\n"
            msg += "-" * 50

            for file in files:
                full = os.path.join(target, file)
                st = os.stat(full)
                mode = stat.filemode(st.st_mode)
                size = st.st_size
                mtime = datetime.datetime.fromtimestamp(st.st_mtime).strftime('%Y-%m-%d %H:%M')

                msg += f"{mode} {size:>10} {mtime} {file}\n"

            msg += "-" * 50

            console_logger.info(msg)