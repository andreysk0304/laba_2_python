from dataclasses import dataclass
from functools import cached_property

from src.utils.tokenizer import tokenizer

@dataclass
class Command:
    input: str

    def __post_init__(self):
        self._tokens = self._get_tokens()


    def _get_tokens(self) -> list:

        tokens = tokenizer(self.input)

        return tokens

    @cached_property
    def flags(self) -> list[str]:
        flags = [token for token in self._tokens if token.startswith('-')]

        return flags

    @cached_property
    def paths(self) -> list[str]:
        paths = [token for token in self._tokens[1:] if not token.startswith('-')]

        return paths

    @cached_property
    def command(self) -> str:
        try:
            return self._tokens[0]
        except IndexError:
            return ''