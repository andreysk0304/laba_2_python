from src.decorators.register_command import register_command, HANDLERS, HANDLERS_DESCRIPTION

from src.components.command import Command

@register_command('help', 'Команда выводит все команды кастомного shell "Андрюшка" и их короткое описание.')
def help_func(command: Command):
    for number, command in enumerate(HANDLERS_DESCRIPTION, 1):
        print(f'{number}. {command} - {HANDLERS_DESCRIPTION[command]}')