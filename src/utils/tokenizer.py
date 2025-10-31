import shlex


def tokenizer(command: str | None) -> list[str]:
    '''
    Разбивает команду на токены.

    :param command: Входная строка в консоле.
    :return: Список токенов в команде.
    '''

    if not command:
        return []

    tokens = shlex.split(command)
    return tokens