import logging


def log_print(message: str, active_logging: bool = True):
    if active_logging:
        logging.error(message)
    print(message)