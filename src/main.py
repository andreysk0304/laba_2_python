import logging

from sys import stdin

from src.commands import *

from src.components.shell import Shell
from src.components.command import Command

from src.decorators.register_command import HANDLERS
from src.utils.messages import log_print

logging.basicConfig(
    filename='shell.log',
    filemode='a',
    level=logging.INFO,
    format='[ %(asctime)s ] %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    encoding='utf-8'
)


def use_command(input_command: str) -> None:
    logging.info(f'{input_command}')
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
                log_print(message=f'{error}')

            return

    log_print(f'command {input_command} not found')


def main() -> None:
    print('Добро пожаловать в кастомный shell "Андрюшка", чтобы отключить его необходимо ввести "exit" или "break"\n\nВведите "help", чтобы увидеть все доступные команды.')

    while stdin:
        command: str = input(f'{Shell.current_path}>')

        if command.strip() in ('exit', 'break'):
            print('Пока пока, до новых встреч :3')

            break

        use_command(input_command=command)

if __name__ == '__main__':
    main()