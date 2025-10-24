import datetime
import json
import os
import shutil

from pathlib import Path


class ShellClass:

    def __init__(self):
        self.current_path = os.path.abspath(os.sep)

        self.trash_path = os.path.join(os.getcwd(), ".trash")
        self.backup_path = os.path.join(os.getcwd(), ".backup")
        self.undo_path = os.path.join(os.getcwd(), ".undo")

        self._ensure_trash_dir()
        self._ensure_backup_dir()
        self._ensure_undo_json()


    def _ensure_trash_dir(self) -> None:
        '''
        Создаёт директорию для мусорки.

        :return: Создаёт директорию .trash
        '''

        os.makedirs(self.trash_path, exist_ok=True)


    def _ensure_backup_dir(self):
        '''
        Создаёт директорию для бэкапов файлов.

        :return: Создаёт диреакторию .backup
        '''

        os.makedirs(self.backup_path, exist_ok=True)


    def _ensure_undo_json(self) -> None:
        '''
        Проверяем наличие json файла .undo

        :return: Создаём его если нет
        '''

        if not Path(self.undo_path).exists():
            with open(self.undo_path, 'w', encoding='utf-8') as file:
                json.dump({'updated_at': str(datetime.datetime.now()), 'operations': []}, file, ensure_ascii=False, indent=4)


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


    def _add_undo_log(self, old_path: str, new_path: str,  operation: str, backup_path: str = '') -> None:
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
                'new_path': new_path,
                'backup_path': backup_path
            }
        )

        with open(self.undo_path, 'w', encoding='utf-8') as file:
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


    def move_file_directory_to_trash(self, input_path: str) -> None:
        '''
        Перемещает файл в корзину.

        :param path: Путь до файла (от корня)
        :return: Путь до файла в корзине (от корня)
        '''

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        path = Path(input_path)

        trash_file_name: str = f"{timestamp}_{path.name}"
        trash_file_path: str = f"{self.trash_path}/{trash_file_name}"

        shutil.move(path, trash_file_path)

        self._add_undo_log(old_path=input_path, new_path=trash_file_path, operation='rm')


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


    def copy_file_or_directory(self, new_path: str, old_path: str) -> None:

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        path = Path(old_path)

        backup_file_name: str = f"{timestamp}_{path.name}"
        backup_file_path: str = f"{self.backup_path}/{backup_file_name}"

        shutil.copy2(Path(old_path), Path(new_path))
        shutil.copy2(Path(old_path), Path(backup_file_path))

        self._add_undo_log(old_path=old_path, new_path=new_path, backup_path=backup_file_path, operation='cp')

        return

Shell = ShellClass()