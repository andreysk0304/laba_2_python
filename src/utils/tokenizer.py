import shlex


def tokenizer(command: str) -> list[str]:
    '''
    Разбивает команду на токены.

    :param command: Входная строка в консоле.
    :return: Список токенов в команде.
    '''

    tokens = shlex.split(command)[1:]

    return tokens