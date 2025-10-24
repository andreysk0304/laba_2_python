from src.decorators.register_command import register_command


@register_command('clear', 'Очищает консоль ввода.')
def clear_func(command: str = None) -> None:
    '''
    Команда очищает консоль (имитирует очистку обычными переносами строк)

    :return: очищает консоль
    '''

    print("\n" * 100)