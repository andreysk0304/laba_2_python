import logging
import sys


def setup_loggers():
    """Настройка трех логеров с разными форматтерами"""

    file_formatter = logging.Formatter('[ %(asctime)s ] %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    console_formatter = logging.Formatter('%(message)s')

    # 1. Логер для консоли и файла
    console_file_logger = logging.getLogger('console_file')
    console_file_logger.setLevel(logging.INFO)
    console_file_logger.propagate = False
    file_handler1 = logging.FileHandler('shell.log', mode='a', encoding='utf-8')
    file_handler1.setFormatter(file_formatter) # Для файла
    console_handler1 = logging.StreamHandler(sys.stdout)
    console_handler1.setFormatter(console_formatter) # Для консоли
    console_file_logger.addHandler(file_handler1)
    console_file_logger.addHandler(console_handler1)

    # 2. Логер только для файла (полная информация)
    file_only_logger = logging.getLogger('file_only')
    file_only_logger.setLevel(logging.INFO)
    file_handler2 = logging.FileHandler('shell.log', mode='a', encoding='utf-8')
    file_handler2.setFormatter(file_formatter)  # Для файла
    file_only_logger.addHandler(file_handler2)

    # 3. Логер только для консоли (только сообщение)
    console_only_logger = logging.getLogger('console_only')
    console_only_logger.setLevel(logging.INFO)
    console_handler2 = logging.StreamHandler(sys.stdout)
    console_handler2.setFormatter(console_formatter)  # Для косноли
    console_only_logger.addHandler(console_handler2)

    return console_file_logger, file_only_logger, console_only_logger


# Инициализация логеров
full_logger, file_logger, console_logger = setup_loggers()