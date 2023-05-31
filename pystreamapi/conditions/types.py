from typing import Type


def of_type(cls: Type):
    return lambda x: isinstance(x, cls)


def not_of_type(cls: Type):
    return lambda x: not isinstance(x, cls)


def none():
    return lambda x: x is None


def not_none():
    return lambda x: x is not None


def true():
    return lambda x: x is True


def not_true():
    return lambda x: x is not True


def false():
    return lambda x: x is False


def not_false():
    return lambda x: x is not False


def length(x):
    return lambda y: len(y) == x


def not_length(x):
    return lambda y: len(y) != x


def empty():
    return lambda x: not x


def not_empty():
    return bool


def equal(x):
    return lambda y: x == y


def not_equal(x):
    return lambda y: x != y
