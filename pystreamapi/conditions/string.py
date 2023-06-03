# Collection of string conditions for use with Stream.filter()
import re


def contains(x: str):
    return lambda y: x in y


def not_contains(x: str):
    return lambda y: x not in y


def starts_with(x: str):
    return lambda y: y.startswith(x)


def ends_with(x: str):
    return lambda y: y.endswith(x)


def matches(x: str):
    return lambda y: re.match(x, y)


def not_matches(x: str):
    return lambda y: not re.match(x, y)


def longer_than(x: int):
    return lambda y: len(y) > x


def shorter_than(x: int):
    return lambda y: len(y) < x


def longer_than_or_equal(x: int):
    return lambda y: len(y) >= x


def shorter_than_or_equal(x: int):
    return lambda y: len(y) <= x


def equal_to_ignore_case(x: str):
    return lambda y: x.lower() == y.lower()


def not_equal_to_ignore_case(x: str):
    return lambda y: x.lower() != y.lower()


def contains_ignore_case(x: str):
    return lambda y: x.lower() in y.lower()


def not_contains_ignore_case(x: str):
    return lambda y: x.lower() not in y.lower()


def starts_with_ignore_case(x: str):
    return lambda y: y.lower().startswith(x.lower())


def ends_with_ignore_case(x: str):
    return lambda y: y.lower().endswith(x.lower())


def matches_ignore_case(x: str):
    return lambda y: re.match(x, y, re.IGNORECASE)


def not_matches_ignore_case(x: str):
    return lambda y: not re.match(x, y, re.IGNORECASE)
