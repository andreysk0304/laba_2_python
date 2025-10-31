import re
import os

from src.decorators.register_command import register_command

from src.components.command import Command
from src.components.shell import Shell

from src.utils.messages import log_print


@register_command('grep', 'Поиск строк по шаблону в файлах. Использование: grep [-r] [-i] <pattern> <path>')
def grep_func(command: Command) -> None:
    if len(command.paths) < 2:
        log_print('Usage: grep [-r] [-i] <pattern> <path>')
        return

    pattern, path = command.paths[0], command.paths[1]
    resolved_path = Shell.resolve_path(path)

    try:
        regex = re.compile(pattern, re.IGNORECASE if '-i' in command.flags else 0)
    except:
        log_print('Invalid pattern')
        return

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
        log_print('Path not found')
        return

    # Все вхождения по файлам
    file_matches = {}

    for file in files:
        try:
            with open(file, 'r', encoding='utf-8', errors='ignore') as f:
                matches = []
                for i, line in enumerate(f, 1):
                    if regex.search(line):
                        matches.append((i, line.strip()))
                if matches:
                    file_matches[file] = matches
        except:
            continue

    if not file_matches:
        log_print('No matches found')
        return

    for file, matches in file_matches.items():
        print(f'___ {file} ___')
        for line_num, line_text in matches:
            print(f'{line_num}. {line_text}')

        print('')