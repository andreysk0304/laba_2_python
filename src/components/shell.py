import datetime
import json
import os
import shutil

from pathlib import Path


class ShellClass:

    def __init__(self):
        self.current_path = os.path.abspath(os.sep)

        self.trash_path = os.path.join(os.getcwd(), ".trash")
        self.undo_path = os.path.join(os.getcwd(), ".undo")
        self.history_path = os.path.join(os.getcwd(), ".history")

        self._ensure_trash_dir()
        self._ensure_undo_json()
        self._ensure_history_json()


    def _ensure_trash_dir(self) -> None:
        '''
        Создаёт директорию для мусорки.

        :return: Создаёт директорию .trash
        '''

        os.makedirs(self.trash_path, exist_ok=True)


    def _ensure_undo_json(self) -> None:
        '''
        Проверяем наличие json файла .undo

        :return: Создаём его если нет
        '''

        if not Path(self.undo_path).exists():
            with open(self.undo_path, 'w', encoding='utf-8') as file:
                json.dump({'updated_at': str(datetime.datetime.now()), 'operations': []}, file, ensure_ascii=False, indent=4)


    def _ensure_history_json(self) -> None:
        '''
        Проверяем наличие json файла .history

        :return: Создаём его если нет
        '''

        if not Path(self.history_path).exists():
            with open(self.history_path, 'w', encoding='utf-8') as file:
                json.dump({'updated_at': str(datetime.datetime.now()), 'operations': []}, file, ensure_ascii=False, indent=4)


    def get_history_json(self) -> dict:
        '''
        Получаем содержимое .history

        :return: Содержимое .history
        '''

        if not Path(self.history_path).exists():
            self._ensure_history_json()

            return {'updated_at': str(datetime.datetime.now()), 'operations': []}

        with open(self.history_path, 'r', encoding='utf-8') as file:
            return json.load(file)


    def _get_undo_json(self) -> dict:
        '''
        Получаем содержимое .undo

        :return: Содержимое .undo
        '''

        if not Path(self.undo_path).exists():
            self._ensure_undo_json()

            return {'updated_at': str(datetime.datetime.now()), 'operations': []}

        with open(self.undo_path, 'r', encoding='utf-8') as file:
            return json.load(file)


    def _add_undo_log(self, old_path: str, new_path: str,  operation: str) -> None:
        '''
        Создаём лог для команды undo

        :param old_path: Старый путь до файла ( до попадания в трэш допустим )
        :param new_path: Новый путь до файла
        :param operation: Тип проведённой операции
        :return: Ничего
        '''

        data = self._get_undo_json()

        data['updated_at'] = str(datetime.datetime.now())

        data['operations'].append(
            {
                'timestamp': str(datetime.datetime.now()),
                'operation': operation,
                'old_path': old_path,
                'new_path': new_path
            }
        )

        with open(self.undo_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


    def add_history_log(self, command: str) -> None:

        data = self.get_history_json()

        data['updated_at'] = str(datetime.datetime.now())

        data['operations'].append(
            {
                'timestamp': str(datetime.datetime.now()),
                'operation': command
            }
        )

        with open(self.history_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


    def _remove_undo_log(self):
        '''
        Удаляет последнее действие из .undo

        :return: Ничего
        '''

        data = self._get_undo_json()

        data['operations'].pop()

        with open(self.undo_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


    def cler_path(self) -> None:
        '''
        Очищаем текущий путь до корневой позиции.

        :return: Очищает текущий абсолютный путь
        '''

        self.current_path = os.path.abspath(os.sep)


    def resolve_path(self, path: str) -> str:
        '''
        Преобразует относительный путь в абсолютный.

        :param path: путь указанный в команде
        :return: новый путь
        '''

        if path == '~':
            return os.path.expanduser('~')

        if os.path.isabs(path):
            return os.path.normpath(path)

        return os.path.normpath(os.path.join(self.current_path, path))


    def move_file_directory_to_trash(self, from_path: str, recursive: bool) -> None:
        '''
        Перемещает файл в корзину.

        :param path: Путь до файла (от корня)
        :return: Путь до файла в корзине (от корня)
        '''

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        path = Path(from_path)

        trash_file_name: str = f"{timestamp}_{path.name}"
        trash_file_path: str = f"{self.trash_path}/{trash_file_name}"

        if path.is_dir() and not recursive:
            return

        shutil.move(path, trash_file_path)

        self._add_undo_log(old_path=from_path, new_path=trash_file_path, operation='rm')


    def get_last_operation_name(self) -> str:
        '''
        Выдаёт последнюю операцию сохранённую в undo.

        :return: Последняя команда для undo
        '''

        data: dict = self.get_last_operation()

        return data.get('operation', '')


    def get_last_operation(self) -> dict:
        '''
        Выдаёт dict последней записи в undo

        :return: последняя запись в undo
        '''

        data = self._get_undo_json()

        if len(data['operations']) == 0:
            return {}

        return data['operations'][-1]


    def move_file_directory_from_trash(self) -> None:
        '''
        Отменяет последнее действие записанное в .undo

        :return: Ничего
        '''

        data = self._get_undo_json()

        if not data['operations']:
            return

        undo_info = data['operations'][-1]

        if undo_info.get('operation', '') == 'rm':
            shutil.move(Path(undo_info['new_path']), Path(undo_info['old_path']))

            self._remove_undo_log()

        else:
            pass

    def copy_file_or_directory(self, from_path: str, to_path: str) -> None:
        from_path = Path(self.resolve_path(from_path))
        to_path = Path(self.resolve_path(to_path))

        if to_path.is_dir():
            to_path = to_path / from_path.name

        if from_path.parent == to_path.parent and from_path.name == to_path.name:
            name, ext = os.path.splitext(to_path.name)
            to_path = to_path.parent / f"{name}_copy{ext}"

        if from_path.is_dir():
            shutil.copytree(from_path, to_path)
        else:
            shutil.copy2(from_path, to_path)

        self._add_undo_log(old_path=str(from_path), new_path=str(to_path), operation='cp')


    def move_file_or_directory(self, from_path: str, to_path: str) -> None:
        from_path = Path(self.resolve_path(from_path))
        to_path = Path(self.resolve_path(to_path))

        if to_path.is_dir():
            to_path = to_path / from_path.name

        shutil.move(str(from_path), str(to_path))
        self._add_undo_log(old_path=str(from_path), new_path=str(to_path), operation='mv')

        return


    def move_file_or_directory_back(self):
        data = self.get_last_operation()

        self.move_file_or_directory(to_path=data['old_path'], from_path=data['new_path'])

        self._remove_undo_log()

        return


    def remove_copied_file_or_directory(self):
        '''
        Удаляет созданную копию файла.

        :return: ничег.
        '''

        data = self.get_last_operation()

        new_path = Path(data['new_path'])

        os.remove(path=new_path)

        self._remove_undo_log()

        return


Shell = ShellClass()