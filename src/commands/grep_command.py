import re
import os

from src.decorators.register_command import register_command

from src.components.command import Command
from src.components.shell import Shell
from src.exceptions.exceptions import InvalidArgumentsCount, InvalidRePattern, PathNotFound, NoMatchesFound
from src.utils.loggers import console_logger


@register_command('grep', 'Поиск строк по шаблону в файлах. Использование: grep [-r] [-i] <pattern> <path>')
def grep_func(command: Command) -> None:
    '''
    Функция ищет в указанной директории вхождения подстрок в файлы

    :param command: Команда из консоли
    :return: Вхождения файл, номер строки, строка
    '''

    if len(command.paths) != 2:
        raise InvalidArgumentsCount(command.command)

    pattern, path = command.paths[0], command.paths[1]
    resolved_path = Shell.resolve_path(path)

    try:
        regex = re.compile(pattern, re.IGNORECASE if '-i' in command.flags else 0)
    except:
        raise InvalidRePattern(pattern)

    # Поиск файлов
    files = []

    if os.path.isfile(resolved_path):
        files = [resolved_path]
    elif os.path.isdir(resolved_path):
        if '-r' in command.flags:
            for root, _, filenames in os.walk(resolved_path):
                files.extend(os.path.join(root, file) for file in filenames)
        else:
            files = [os.path.join(resolved_path, file) for file in os.listdir(resolved_path) if os.path.isfile(os.path.join(resolved_path, file))]
    else:
        raise PathNotFound(path)

    # Все вхождения по файлам
    file_matches = {}

    for file in files:
        try:
            with open(file, 'r',encoding='utf-8', errors='ignore') as f:
                matches = []
                for i, line in enumerate(f, 1):
                    if regex.search(line):
                        matches.append((i, line.strip()))
                if matches:
                    file_matches[file] = matches
        except:
            continue

    if not file_matches:
        raise NoMatchesFound(pattern)

    msg: str = ''
    for file, matches in file_matches.items():
        msg += f'___ {file} ___'
        for line_num, line_text in matches:
            msg += f'{line_num}. {line_text}\n'

        console_logger.info(msg + '\n')