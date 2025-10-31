from src.decorators.register_command import register_command, HANDLERS, HANDLERS_DESCRIPTION

from src.components.command import Command
from src.utils.loggers import console_logger


@register_command('help', 'Команда выводит все команды кастомного shell "Андрюшка" и их короткое описание.')
def help_func(command: Command):
    '''
    Функция выводит все доступные команды с их описание (если есть) в консоль пользователю

    :param command: Конада из консоли
    :return: Список команд с их описанием
    '''

    for number, command in enumerate(HANDLERS_DESCRIPTION, 1):
        console_logger.info(f'{number}. {command} - {HANDLERS_DESCRIPTION[command]}')