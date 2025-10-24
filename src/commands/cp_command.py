from src.decorators.register_command import register_command
from src.utils.messages import log_print
from src.utils.tokenizer import tokenizer


@register_command('cp', 'Команда cp <from_path> <to_path> копирует файл из <from_path> в <to_path>')
def cp_func(command: str) -> None:

    tokens = tokenizer(command=command)

    if not len(tokens) == 2:
        log_print('params error.')

        return

    from_path, to_path = tokens[0], tokens[1]