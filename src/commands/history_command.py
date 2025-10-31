from src.decorators.register_command import register_command

from src.utils.tokenizer import tokenizer
from src.utils.messages import log_print

from src.components.shell import Shell
from src.components.command import Command


@register_command('history', 'Показывает посленднее n кол-во вписаных команд.')
def history_func(command: Command):
    n: int = 25

    if command.paths:
        if command.paths[-1].isdigit():
            n = int(command.paths[-1])
        else:
            log_print('Not correct command params.')

    history_data = Shell.get_history_json()

    msg: str = ''

    for number, operation_log in enumerate(reversed(history_data['operations']), 1):
        msg = f'{number}. {operation_log["operation"]}\n' + msg
        if number == n:
            break

    print(msg)