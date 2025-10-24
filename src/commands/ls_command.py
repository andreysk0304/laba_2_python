import os
import logging
import stat
import datetime

from src.utils.tokenizer import tokenizer

from src.components.shell import Shell
from src.decorators.register_command import register_command


@register_command('ls', 'Выводит в консоль всё содержимое текущей директории. Флаг -l позволяет увидеть расширенную информацию, пример ввода: ls -l')
def ls_func(command: str) -> None:
    long: bool = False # включён ли флаг -l

    tokens = tokenizer(command)

    if '-l' in tokens:
        long = True

    paths = [token for token in tokens if not token.startswith('-')]

    if not paths:
        paths.append('')

    for path in paths:
        if path == '' or path == ' ':
            path = '.'

        target = Shell.resolve_path(path)

        try:
            files = os.listdir(target)

        except FileNotFoundError:
            logging.error(f"directory '{target}' not found.")

            print(f"directory '{target}' not found.")

            return

        except PermissionError:
            logging.error(f"You have not got permissions to '{target}'")

            print(f"You have not got permissions to '{target}'")

            return

        if not long:
            print(f'\n>{path}')

            for file in files:
                print(file)

            print("-" * 50)

        else:
            print(f'\n>{path}')
            print(f"{'MODE':<11} {'SIZE':>10} {'LAST MODIFIED':<17} NAME")
            print("-" * 50)

            for file in files:
                full = os.path.join(target, file)

                st = os.stat(full)
                mode = stat.filemode(st.st_mode)
                size = st.st_size

                mtime = datetime.datetime.fromtimestamp(st.st_mtime).strftime('%Y-%m-%d %H:%M')

                print(f"{mode} {size:>10} {mtime} {file}")

            print("-" * 50)