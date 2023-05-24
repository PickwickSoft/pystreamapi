# Collection of numeric conditions for use with Stream.filter()
import math as __math
from datetime import datetime as __datetime
from typing import overload as __overload, Callable as __Callable, Any as __Any


def even(n):
    return n % 2 == 0


def odd(n):
    return n % 2 != 0


def positive(n):
    return n > 0


def negative(n):
    return n < 0


def zero(n):
    return n == 0


def non_zero(n):
    return n != 0


def greater_than(n):
    return lambda y: y > n


def greater_than_or_equal(n):
    return lambda y: y >= n


def less_than(n):
    return lambda y: y < n


def less_than_or_equal(n):
    return lambda y: y <= n


@__overload
def between(minimum: __datetime, maximum: __datetime) -> __Callable[[__datetime], bool]:
    """
    Returns a condition that checks if a datetime is between two given datetimes.
    :param minimum: The datetime to check against.
    :param maximum: The datetime to check against.
    :return: A condition that checks if a datetime is between two given datetimes.
    """


def between(minimum, maximum) -> __Callable[[__Any], bool]:
    return lambda n: minimum <= n <= maximum


@__overload
def not_between(minimum: __datetime, maximum: __datetime) -> __Callable[[__datetime], bool]:
    """
    Returns a condition that checks if a datetime is not between two given datetimes.
    :param minimum: The datetime to check against.
    :param maximum: The datetime to check against.
    :return: A condition that checks if a datetime is not between two given datetimes.
    """


def not_between(minimum, maximum) -> __Callable[[__Any], bool]:
    return lambda n: not between(minimum, maximum)(n)


@__overload
def equal_to(d: __datetime):
    """
    Returns a condition that checks if a datetime is equal to a given datetime.
    :param d: The datetime to check against.
    :return: A condition that checks if a datetime is equal to a given datetime.
    """

@__overload
def equal_to(d: str):
    """
    Returns a condition that checks if a string is equal to a given string.
    :param d: The string to check against.
    :return: A condition that checks if a string is equal to a given string.
    """


def equal_to(n):
    return lambda y: y == n


@__overload
def not_equal_to(d: __datetime) -> __Callable[[__datetime], bool]:
    """
    Returns a condition that checks if a datetime is not equal to a given datetime.
    :param d: The datetime to check against.
    :return: A condition that checks if a datetime is not equal to a given datetime.
    """

@__overload
def not_equal_to(d: str) -> __Callable[[str], bool]:
    """
    Returns a condition that checks if a string is not equal to a given string.
    :param d: The string to check against.
    :return: A condition that checks if a string is not equal to a given string.
    """


def not_equal_to(n) -> __Callable[[__Any], bool]:
    return lambda y: y != n


def multiple_of(n):
    return lambda y: y % n == 0


def not_multiple_of(n):
    return lambda y: not multiple_of(n)(y)


def divisor_of(n):
    return lambda y: n % y == 0


def not_divisor_of(n):
    return lambda y: not divisor_of(n)(y)


def prime(n):
    return n > 1 and all(n % i for i in range(2, n))


def not_prime(n):
    return not prime(n)


def perfect_square(n):
    return 0 <= n == int(n ** 0.5) ** 2


def not_perfect_square(n):
    return not perfect_square(n)


def perfect_cube(n):
    return 0 <= n == int(n ** (1 / 3)) ** 3


def not_perfect_cube(n):
    return not perfect_cube(n)


def perfect_power(n):
    return n > 0 and any(
        n == i ** j for i in range(1, int(n ** 0.5) + 1) for j in range(2, int(__math.log2(n)) + 1))


def not_perfect_power(n):
    return not perfect_power(n)


def palindrome(n):
    return str(n) == str(n)[::-1]


def not_palindrome(n):
    return not palindrome(n)


def armstrong(n):
    return n == sum(int(d) ** len(str(n)) for d in str(n))


def not_armstrong(n):
    return not armstrong(n)


def narcissistic(n):
    return n == sum(int(d) ** len(str(n)) for d in str(n))


def not_narcissistic(n):
    return not narcissistic(n)


def happy(n):
    return n == sum(int(d) ** 2 for d in str(n)) if n < 10 \
        else happy(sum(int(d) ** 2 for d in str(n)))


def sad(n):
    return not happy(n)


def abundant(n):
    return sum(i for i in range(1, n) if n % i == 0) > n


def not_abundant(n):
    return not abundant(n)


def deficient(n):
    return sum(i for i in range(1, n) if n % i == 0) < n


def not_deficient(n):
    return not deficient(n)


def perfect(n):
    return n == sum(i for i in range(1, n) if n % i == 0)


def not_perfect(n):
    return not perfect(n)
