from enum import Enum


class ErrorLevel(Enum):
    """
    PyStreamAPI error levels.
    RAISE: raise an exception
    IGNORE: ignore the error, skip the item
    WARN: print a warning and ignore the error
    """

    RAISE = 0
    IGNORE = 1
    WARN = 2
