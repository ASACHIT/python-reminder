import functools
import re
import colorama
from colorama import Fore

# Initialize colorama.
colorama.init()

class _ColorizeMeta(type): # type: dutc
    """
    Meta Class for Colorize. This class is used to dynamically create methods.
    """

    def __getattribute__(cls, name: str):
        if name.startswith("_"):
            return super().__getattribute__(name)
        if match := re.fullmatch(r"([a-zA-Z]+)(_[a-zA-Z]+)", name):
            color, func = match.groups()
            # type: ignore
            return functools.partial(getattr(cls, func), color=color.upper())
        else:
            return functools.partial(cls._colorize, color=name.upper())
        return super().__getattribute__(name)


class Colorize(metaclass=_ColorizeMeta):
    @staticmethod
    def _colorize(text: str, color: str) -> str:
        return getattr(Fore, color) + text + Fore.RESET

    @classmethod
    def _print(cls, text: str, color: str):
        print(cls._colorize(text, color))

    @classmethod
    def _input(cls, text: str, color: str):
        return input(cls._colorize(text, color))

