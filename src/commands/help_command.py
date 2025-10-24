from src.decorators.register_command import register_command, HANDLERS, HANDLERS_DESCRIPTION


@register_command('help', 'Команда выводит все команды кастомного shell "Андрюшка" и их короткое описание.')
def help_func(command: str = None):
    for number, command in enumerate(HANDLERS_DESCRIPTION, 1):
        print(f'{number}. {command} - {HANDLERS_DESCRIPTION[command]}')