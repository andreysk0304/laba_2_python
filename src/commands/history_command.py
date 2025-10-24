from src.decorators.register_command import register_command
from src.utils.tokenizer import tokenizer
from src.utils.messages import log_print


@register_command('history', 'Показывает посленднее n кол-во вписаных команд.')
def history_func(command: str):

    tokens = tokenizer(command)

    n = 25

    if tokens:
        if tokens[-1].isdigit():
            n = int(tokens[-1])

        else:
            log_print('Not correct command params.')

    with open('shell.log', 'r', encoding='utf-8') as file:

        lines = file.readlines()

        lines.reverse()

        number = 0

        msg = ''

        for line in lines:

            if 'INFO: ' in line:
                number += 1

                msg = f'{number}. {line.split("INFO: ")[-1].strip()}\n' + msg

            if number == n:
                break

        print(msg)