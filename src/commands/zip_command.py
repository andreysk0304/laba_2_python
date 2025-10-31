import shutil
import os

from src.components.shell import Shell
from src.decorators.register_command import register_command

from src.utils.messages import log_print

from src.components.command import Command


@register_command('zip', 'Команда создаёт zip <folder> <archive.zip> архив из указанного файла или директории.')
def zip_func(command: Command) -> None:
    if len(command.paths) != 2:
        log_print('Usage: zip <folder> <archive.zip>')
        return

    folder_path, archive_name = command.paths[0], command.paths[1]

    if not archive_name.endswith('.zip'):
        log_print('Invalid name zip file.\nExample: "example.zip"')
        return

    folder_full_path = Shell.resolve_path(folder_path)

    if not os.path.exists(folder_full_path):
        log_print(f'Folder not found: {folder_path}')
        return

    archive_base_name = archive_name[:-4]
    archive_full_path = Shell.resolve_path(archive_base_name)

    shutil.make_archive(archive_full_path, 'zip', folder_full_path)

    log_print(f'Archive created: {archive_name}')


@register_command('tar', 'Команда создаёт tar <folder> <archive.tar> архив из указанного файла или директории.')
def tar_func(command: Command) -> None:
    if len(command.paths) != 2:
        log_print('Usage: tar <folder> <archive.tar>')
        return

    folder_path, archive_name = command.paths[0], command.paths[1]

    if not archive_name.endswith('.tar'):
        log_print('Invalid name tar file.\nExample: "example.tar"')
        return

    folder_full_path = Shell.resolve_path(folder_path)

    if not os.path.exists(folder_full_path):
        log_print(f'Folder not found: {folder_path}')
        return

    archive_base_name = archive_name[:-4]
    archive_full_path = Shell.resolve_path(archive_base_name)

    shutil.make_archive(archive_full_path, 'tar', folder_full_path)

    log_print(f'Archive created: {archive_name}')


@register_command('unzip', 'Команда распаковывает zip <archive.zip> <destination_folder> архив в указанную директорию.')
def unzip_func(command: Command) -> None:
    if len(command.paths) != 2:
        log_print('Usage: unzip <archive.zip> <destination_folder>')
        return

    archive_path, dest_folder = command.paths[0], command.paths[1]

    if not archive_path.endswith('.zip'):
        log_print('Invalid archive file. Must be a .zip file.\nExample: "example.zip"')
        return

    archive_full_path = Shell.resolve_path(archive_path)
    dest_full_path = Shell.resolve_path(dest_folder)

    if not os.path.exists(archive_full_path):
        log_print(f'Archive not found: {archive_path}')
        return

    shutil.unpack_archive(archive_full_path, dest_full_path, 'zip')
    log_print(f'Archive extracted to: {dest_folder}')

    return


@register_command('untar', 'Команда распаковывает tar <archive.tar> <folder> архив в указанную директорию.')
def untar_func(command: Command) -> None:
    if len(command.paths) != 2:
        log_print('Usage: untar <archive.tar> <folder>')
        return

    archive_path, dest_folder = command.paths[0], command.paths[1]

    if not archive_path.endswith('.tar'):
        log_print('Invalid archive file. Must be a .tar file.\nExample: "example.tar"')
        return

    archive_full_path = Shell.resolve_path(archive_path)
    dest_full_path = Shell.resolve_path(dest_folder)

    if not os.path.exists(archive_full_path):
        log_print(f'Archive not found: {archive_path}')
        return

    shutil.unpack_archive(archive_full_path, dest_full_path, 'tar')
    log_print(f'Archive extracted to: {dest_folder}')

    return