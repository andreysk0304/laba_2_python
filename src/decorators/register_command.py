HANDLERS: dict[str, callable] = {}
HANDLERS_DESCRIPTION: dict[str, str] = {}


def register_command(prefix: str, description: str = "Кое-кто не дописал описание :D"):
    '''
    Декоратор для регистрации команд в словарь HANDLERS

    :param prefix: название команды (ls, cd, ...) это ключ для словаря, чтобы потом изьять от туда функцию и вызвать её
    :return: создаёт непосредственно запись в словаре, где мы будем брать функции для вызова
    '''

    def decorator(func: callable):
        HANDLERS[prefix] = func
        HANDLERS_DESCRIPTION[prefix] = description

        return func

    return decorator