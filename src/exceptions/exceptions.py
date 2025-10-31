class InvalidArgumentsCount(Exception):
    def __init__(self, command: str):
        super().__init__(f"Неверное количество аргументов для команды '{command}'.")


class InvalidArgumentsType(Exception):
    def __init__(self):
        super().__init__(f"Не верный тип переданных параметров.")


class FileNotFound(Exception):
    def __init__(self, file: str):
        super().__init__(f"Файл '{file}' не найден.")


class IsDirectory(Exception):
    def __init__(self, path: str):
        super().__init__(f"'{path}' - директория, а не файл.")


class NotEnoughPermissions(Exception):
    def __init__(self):
        super().__init__(f"Не достаточно прав доступа.")
        
        
class IsNotTextFile(Exception):
    def __init__(self):
        super().__init__(f"Это не текстовый файл.")
        
        
class CatalogNotFound(Exception):
    def __init__(self, path: str):
        super().__init__(f"Каталог '{path}' не существует.")
        
        
class CodeError(Exception):
    def __init__(self, error: str):
        super().__init__(f"Упс, непредвиденная ошибка '{error}'.")


class InvalidRePattern(Exception):
    def __init__(self, pattern: str):
        super().__init__(f"Ошибка обработки переданного паттерна '{pattern}'.")


class PathNotFound(Exception):
    def __init__(self, path: str):
        super().__init__(f"Путь '{path}' не найден.")


class NoMatchesFound(Exception):
    def __init__(self, pattern: str):
        super().__init__(f"Вхождения '{pattern}' не найдены.")


class CannotRemove(Exception):
    def __init__(self, path: str):
        super().__init__(f"Нельзя удалить директорию '{path}'")
        

class CannotRemoveNotFound(Exception):
    def __init__(self, path: str):
        super().__init__(f"Нельзя удалить '{path}', файл или директория не найдены.")


class InvalidArchiveName(Exception):
    def __init__(self, arc_type: str):
        super().__init__(f"Не верное название файла архива\n\nПример 'example.{arc_type}'")
        
        
class ArchiveNotFound(Exception):
    def __init__(self):
        super().__init__(f"Архив не найден.")