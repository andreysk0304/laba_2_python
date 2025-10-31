from sys import stdin

from src.commands import *

from src.utils.loggers import full_logger, console_logger, file_logger

from src.components.shell import Shell
from src.components.command import Command

from src.decorators.register_command import HANDLERS

def use_command(input_command: str) -> None:
    file_logger.info(f'{input_command}')
    Shell.add_history_log(command=input_command)

    input_command: str = input_command.strip()

    command: Command = Command(input_command)

    if command.command == '':
        return

    for prefix, handler in HANDLERS.items():
        if command.command == prefix:
            try:
                handler(command)
            except Exception as error:
                full_logger.error(f'{error}')

            return

    full_logger.error(f"Команда '{command.command}' не найдена :(")


def main() -> None:
    console_logger.info('Добро пожаловать в кастомный shell "Андрюшка", чтобы отключить его необходимо ввести "exit" или "break"\n\nВведите "help", чтобы увидеть все доступные команды.')

    while stdin:
        command: str = input(f'{Shell.current_path}>')

        if command.strip() in ('exit', 'break'):
            console_logger.info('Пока пока, до новых встреч :3')

            break

        use_command(input_command=command)

if __name__ == '__main__':
    main()