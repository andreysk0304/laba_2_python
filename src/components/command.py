from dataclasses import dataclass
from functools import cached_property

from src.utils.tokenizer import tokenizer

@dataclass
class Command:
    input: str

    def __post_init__(self):
        self._tokens = self._get_tokens()


    def _get_tokens(self) -> list:
        '''
        Функция токенизирует входную строку

        :return: Список токенов
        '''

        tokens = tokenizer(self.input)

        return tokens

    @cached_property
    def flags(self) -> list[str]:
        '''
        Функция достаёт из списка те токены которые начинаются с "-" их мы называем флагом и кладём в список флагов

        :return: Список флагов
        '''
        flags = [token for token in self._tokens if token.startswith('-')]

        return flags

    @cached_property
    def paths(self) -> list[str]:
        '''
        Функция достаёт из списка те токены которые НЕ начинаются с "-" их мы называем путём и кладём в список путей

        :return: Список путей
        '''
        paths = [token for token in self._tokens[1:] if not token.startswith('-')]

        return paths

    @cached_property
    def command(self) -> str:
        '''
        Функция отдаёт первый токен входной команды, его мы называем самой командой или префиксом

        :return: Префикс команды (cp, rm, ls, cd, ...)
        '''

        try:
            return self._tokens[0]
        except IndexError:
            return ''