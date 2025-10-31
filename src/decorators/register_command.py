HANDLERS: dict[str, callable] = {}
HANDLERS_DESCRIPTION: dict[str, str] = {}


def register_command(prefix: str, description: str = "Кое-кто не дописал описание :D"):
    '''
    Декоратор для регистрации команд в словарь HANDLERS

    :param prefix: название команды (ls, cd, ...) это ключ для словаря, чтобы потом изьять от туда функцию и вызвать её
    :return: создаёт непосредственно запись в словаре, где мы будем брать функции для вызова
    '''

    def decorator(func: callable) -> callable:
        '''
        Функция регистрирует функцию команды по ключу префикса команды, где префикс это (cd, rm, ls, cd, ...).
        Функция регистрирует описание команды по ключу префикса команды.

        :param func: Функция, которая выполняет ту или иную команду.
        :return: Создаёт запись внутри словаря HANDLERS и HANDLERS_DESCRIPRION, возвращает саму функцию (т.к это декоратор).
        '''

        HANDLERS[prefix] = func
        HANDLERS_DESCRIPTION[prefix] = description

        return func

    return decorator