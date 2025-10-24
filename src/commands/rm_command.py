from src.utils.messages import log_print
from src.decorators.register_command import register_command
from src.utils.tokenizer import tokenizer
from src.components.shell import Shell

from pathlib import Path


@register_command('rm', 'Команда rm <path> удаляет указанный файл.')
def rm_func(command: str) -> None:

    tokens = tokenizer(command=command)

    recursive: bool = False

    if '-r' in tokens:
        recursive = True

    paths = [token for token in tokens if not token.startswith('-')]

    if not paths:
        log_print(message='does not have path params.')

        return

    target = Shell.resolve_path(paths[0])

    path = Path(target)

    if path.resolve() == Path('/').resolve():
        log_print(message="cannot remove root directory '/'")

        return

    if path.resolve() == Path('..').resolve() or path.name == '..':
        log_print(message="cannot remove parent directory '..'")

        return

    if path.resolve() == Path('.').resolve() or path.name == '.':
        log_print(message="cannot remove current directory '.'")

        return

    if not path.exists():
        log_print(message=f"cannot remove '{path}', no such file or directory.")

        return

    try:
        check: str = input('you are agree ? y/n\n')

        if check.strip().lower() == 'y':
            Shell.move_file_directory_to_trash(target)

            print(f"you remove: '{path}'")

            return

        else:
            return

    except Exception as error:
        log_print(f'{error}')