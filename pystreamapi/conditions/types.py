from typing import Type


def of_type(cls: Type):
    return lambda x: isinstance(x, cls)


def not_of_type(cls: Type):
    return lambda x: not isinstance(x, cls)


def none(x):
    return x is None


def not_none(x):
    return x is not None


def true(x):
    return x is True


def not_true(x):
    return x is not True


def false(x):
    return x is False


def not_false(x):
    return x is not False


def length(x):
    return lambda y: len(y) == x


def not_length(x):
    return lambda y: len(y) != x


def empty(x):
    return not x


def not_empty(x):
    return bool(x)


def equal(x):
    return lambda y: x == y


def not_equal(x):
    return lambda y: x != y
