from src.decorators.register_command import register_command

from src.components.command import Command


@register_command('clear', 'Очищает консоль ввода.')
def clear_func(command: Command) -> None:
    '''
    Команда очищает консоль (имитирует очистку обычными переносами строк)

    :return: очищает консоль
    '''

    print("\n" * 100)