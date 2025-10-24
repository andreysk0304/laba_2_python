import logging

from src.commands import *

from src.components.shell import Shell

from src.decorators.register_command import HANDLERS

logging.basicConfig(
    filename='shell.log',
    filemode='a',
    level=logging.INFO,
    format='[ %(asctime)s ] %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def use_command(command: str) -> None:
    logging.info(f'{command}')

    command = command.strip()

    for prefix, handler in HANDLERS.items():
        if command == prefix or command.startswith(prefix+' '):
            handler(command)

            return

    print(f"command '{command}' not found.")

    logging.error(f"command '{command}' not found.")


def main() -> None:
    print('Добро пожаловать в кастомный shell "Андрюшка", чтобы отключить его необходимо ввести "exit" или "break"\n\nВведите "help", чтобы увидеть все доступные команды.')

    while True:
        command: str = input(f'{Shell.current_path}>')

        if command.strip() in ('exit', 'break'):
            print('Пока пока, до новых встреч :3')

            break

        use_command(command=command)

if __name__ == '__main__':
    main()