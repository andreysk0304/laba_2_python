import shutil
import os

from src.components.shell import Shell
from src.decorators.register_command import register_command
from src.exceptions.exceptions import InvalidArgumentsCount, InvalidArchiveName, ArchiveNotFound, CatalogNotFound
from src.utils.loggers import console_logger

from src.components.command import Command


@register_command('zip', 'Команда создаёт zip <folder> <archive.zip> архив из указанного файла или директории.')
def zip_func(command: Command) -> None:
    '''
    Функция архивирует директорию/файл в .zip архив

    :param command: Команда из консоли
    :return: Готовый .zip архив
    '''


    if len(command.paths) != 2:
        raise InvalidArgumentsCount(command.command)

    folder_path, archive_name = command.paths[0], command.paths[1]

    if not archive_name.endswith('.zip'):
        raise InvalidArchiveName('zip')

    folder_full_path = Shell.resolve_path(folder_path)

    if not os.path.exists(folder_full_path):
        raise CatalogNotFound(folder_path)

    archive_base_name = archive_name[:-4]
    archive_full_path = Shell.resolve_path(archive_base_name)

    shutil.make_archive(archive_full_path, 'zip', folder_full_path)

    console_logger.info(f'Архив создан: {archive_name}')


@register_command('tar', 'Команда создаёт tar <folder> <archive.tar> архив из указанного файла или директории.')
def tar_func(command: Command) -> None:
    '''
    Функция архивирует директорию/файл в .tar архив

    :param command: Команда из консоли
    :return: Готовый .tar архив
    '''
    if len(command.paths) != 2:
        raise InvalidArgumentsCount(command.command)

    folder_path, archive_name = command.paths[0], command.paths[1]

    if not archive_name.endswith('.tar'):
        raise InvalidArchiveName('tar')

    folder_full_path = Shell.resolve_path(folder_path)

    if not os.path.exists(folder_full_path):
        raise CatalogNotFound(folder_path)

    archive_base_name = archive_name[:-4]
    archive_full_path = Shell.resolve_path(archive_base_name)

    shutil.make_archive(archive_full_path, 'tar', folder_full_path)

    console_logger.info(f'Архив создан: {archive_name}')


@register_command('unzip', 'Команда распаковывает zip <archive.zip> <folder> архив в указанную директорию.')
def unzip_func(command: Command) -> None:
    '''
    Функция распаковывает из .zip архива директорию/файл в указанный путь <folder>

    :param command: Команда из консоли
    :return: Ничего
    '''

    if len(command.paths) != 2:
        raise InvalidArgumentsCount(command.command)

    archive_path, dest_folder = command.paths[0], command.paths[1]

    if not archive_path.endswith('.zip'):
        raise InvalidArchiveName('zip')

    archive_full_path = Shell.resolve_path(archive_path)
    dest_full_path = Shell.resolve_path(dest_folder)

    if not os.path.exists(archive_full_path):
        raise ArchiveNotFound()

    shutil.unpack_archive(archive_full_path, dest_full_path, 'zip')
    console_logger.info(f'Архив распакован в {dest_folder}')

    return


@register_command('untar', 'Команда распаковывает tar <archive.tar> <folder> архив в указанную директорию.')
def untar_func(command: Command) -> None:
    '''
    Функция распаковывает из .tar архива директорию/файл в указанный путь <folder>

    :param command: Команда из консоли
    :return: Ничего
    '''

    if len(command.paths) != 2:
        raise InvalidArgumentsCount(command.command)

    archive_path, dest_folder = command.paths[0], command.paths[1]

    if not archive_path.endswith('.tar'):
        raise InvalidArchiveName('tar')

    archive_full_path = Shell.resolve_path(archive_path)
    dest_full_path = Shell.resolve_path(dest_folder)

    if not os.path.exists(archive_full_path):
        raise ArchiveNotFound()

    shutil.unpack_archive(archive_full_path, dest_full_path, 'tar')
    console_logger.info(f'Архив распокован в {dest_folder}')

    return