from datetime import datetime as __datetime, timedelta as __timedelta, timezone as __timezone, \
    date as __date
from typing import Union


def before(d: Union[__datetime, __date]):
    """
    Returns a condition that checks if a datetime is before a given datetime.
    :param d: The datetime to check against.
    :return: A condition that checks if a datetime is before a given datetime.
    """
    return lambda y: y < d


def after(d: Union[__datetime, __date]):
    """
    Returns a condition that checks if a datetime is after a given datetime.
    :param d: The datetime to check against.
    :return: A condition that checks if a datetime is after a given datetime.
    """
    return lambda y: y > d


def before_or_equal(d: Union[__datetime, __date]):
    """
    Returns a condition that checks if a datetime is before or equal to a given datetime.
    :param d: The datetime to check against.
    :return: A condition that checks if a datetime is before or equal to a given datetime.
    """
    return lambda y: y <= d


def after_or_equal(d: Union[__datetime, __date]):
    """
    Returns a condition that checks if a datetime is after or equal to a given datetime.
    :param d: The datetime to check against.
    :return: A condition that checks if a datetime is after or equal to a given datetime.
    """
    return lambda y: y >= d


def between_or_equal(d: Union[__datetime, __date], y: Union[__datetime, __date]):
    """
    Returns a condition that checks if a datetime is between or equal to two given datetimes.
    :param d: The datetime to check against.
    :param y: The datetime to check against.
    :return: A condition that checks if a datetime is between or equal to two given datetimes.
    """
    return lambda z: d <= z <= y


def not_between_or_equal(d: Union[__datetime, __date], y: Union[__datetime, __date]):
    """
    Returns a condition that checks if a datetime is not between or equal to two given datetimes.
    :param d: The datetime to check against.
    :param y: The datetime to check against.
    :return: A condition that checks if a datetime is not between or equal to two given datetimes.
    """
    return lambda z: not d <= z <= y


def today():
    """
    The condition that checks if a datetime is today.
    :return: A condition that checks if a datetime is today.
    """
    return lambda d: __datetime.now().date() == d.date() if isinstance(d, __datetime) else \
        __datetime.now().date() == d


def today_utc():
    """
    The condition that checks if a datetime is today calculating in UTC (use without parenthesis
    in your Stream).
    :return: A condition that checks if a datetime is today.
    """
    return lambda d: __datetime.now(__timezone.utc).date() == d.astimezone(__timezone.utc).date() \
        if isinstance(d, __datetime) else __datetime.now(__timezone.utc).date() == d


def yesterday():
    """
    The condition that checks if a datetime is yesterday.
    :return: A condition that checks if a datetime is yesterday.
    """
    return lambda d: __datetime.now().date() - __timedelta(days=1) == d.date() if \
        isinstance(d, __datetime) else __datetime.now().date() - __timedelta(days=1) == d


def yesterday_utc():
    """
    The condition that checks if a datetime is yesterday calculating in UTC (use without
    parenthesis in your Stream).
    :return: A condition that checks if a datetime is yesterday.
    """
    return lambda d: __datetime.now(__timezone.utc).date() - __timedelta(days=1) == d.astimezone(
        __timezone.utc).date() if isinstance(d, __datetime) \
        else __datetime.now(__timezone.utc).date() - __timedelta(days=1) == d


def tomorrow():
    """
    A condition that checks if a datetime is tomorrow.
    :return: A condition that checks if a datetime is tomorrow.
    """
    return lambda d: __datetime.now().date() + __timedelta(days=1) == d.date() if \
        isinstance(d, __datetime) else __datetime.now().date() + __timedelta(days=1) == d


def tomorrow_utc():
    """
    A condition that checks if a datetime is tomorrow calculating in UTC (use without parenthesis
    in your Stream).
    :return: A condition that checks if a datetime is tomorrow.
    """
    return lambda d: __datetime.now(__timezone.utc).date() + __timedelta(days=1) == d.astimezone(
        __timezone.utc).date() if isinstance(d, __datetime) \
        else __datetime.now(__timezone.utc).date() + __timedelta(days=1) == d


def this_week():
    """
    A condition that checks if a datetime is this week.
    :return: A condition that checks if a datetime is this week.
    """
    return __check_is_week


def this_week_utc():
    """
    A condition that checks if a datetime is this week calculating in UTC (use without
    parenthesis in your Stream).
    :return: A condition that checks if a datetime is this week.
    """
    return lambda d: __check_is_week(d, tz=__timezone.utc)


def last_week():
    """
    A condition that checks if a datetime is last week.
    :return: A condition that checks if a datetime is last week.
    """
    return lambda d: __check_is_week(d, -1)


def last_week_utc():
    """
    A condition that checks if a datetime is last week calculating in UTC (use without
    parenthesis in your Stream).
    :return: A condition that checks if a datetime is last week.
    """
    return lambda d: __check_is_week(d, -1, tz=__timezone.utc)


def next_week():
    """
    A condition that checks if a datetime is next week.
    :return: A condition that checks if a datetime is next week.
    """
    return lambda d: __check_is_week(d, 1)


def next_week_utc():
    """
    A condition that checks if a datetime is next week calculating in UTC (use without
    parenthesis in your Stream).
    :return: A condition that checks if a datetime is next week.
    """
    return lambda d: __check_is_week(d, 1, tz=__timezone.utc)


def __check_is_week(d: Union[__datetime, __date], offset: int = 0, tz: __timezone = None):
    target_week = __datetime.now(tz=tz) + __timedelta(weeks=offset)
    return target_week.isocalendar()[1] == d.date().isocalendar()[1] if \
        isinstance(d, __datetime) \
        else target_week.isocalendar()[1] == d.isocalendar()[1]


def this_month():
    """
    A condition that checks if a datetime is this month.
    :return: A condition that checks if a datetime is this month.
    """
    return __check_is_month


def this_month_utc():
    """
    A condition that checks if a datetime is this month calculating in UTC (use without
    parenthesis in your Stream).
    :return: A condition that checks if a datetime is this month.
    """
    return lambda d: __check_is_month(d, tz=__timezone.utc)


def last_month():
    """
    A condition that checks if a datetime is last month.
    :return: A condition that checks if a datetime is last month.
    """
    return lambda d: __check_is_month(d, -1)


def last_month_utc():
    """
    A condition that checks if a datetime is last month calculating in UTC (use without
    parenthesis in your Stream).
    :return: A condition that checks if a datetime is last month.
    """
    return lambda d: __check_is_month(d, -1, tz=__timezone.utc)


def next_month():
    """
    A condition that checks if a datetime is next month.
    :return: A condition that checks if a datetime is next month.
    """
    return lambda d: __check_is_month(d, 1)


def next_month_utc():
    """
    A condition that checks if a datetime is next month calculating in UTC (use without
    parenthesis in your Stream).
    :return: A condition that checks if a datetime is next month.
    """
    return lambda d: __check_is_month(d, 1, tz=__timezone.utc)


def __check_is_month(d: Union[__datetime, __date], offset: int = 0, tz: __timezone = None):
    """
    The actual function that checks if a datetime is a specific month also supporting
    UTC timezone and offsets.
    :param d: The datetime to check against.
    :param offset: The offset to check against.
    :param tz: The timezone to check against.
    """
    month = __datetime.now(tz).date().month + offset
    month = reduce_to_valid_range(month, 12)
    return month == d.astimezone(tz).date().month if \
        isinstance(d, __datetime) else month == d.month


def this_year():
    """
    A condition that checks if a datetime is this year.
    :return: A condition that checks if a datetime is this year.
    """
    return __check_is_year


def this_year_utc():
    """
    A condition that checks if a datetime is this year calculating in UTC (use without
    parenthesis in your Stream).
    """
    return lambda d: __check_is_year(d, tz=__timezone.utc)


def last_year():
    """
    A condition that checks if a datetime is from last year.
    :return: A condition that checks if a datetime is from last year.
    """
    return lambda d: __check_is_year(d, -1)


def last_year_utc():
    """
    A condition that checks if a datetime is last year calculating in UTC (use without
    parenthesis in your Stream).
    :return: A condition that checks if a datetime is from last year.
    """
    return lambda d: __check_is_year(d, -1, tz=__timezone.utc)


def next_year():
    """
    A condition that checks if a datetime is next year.
    :return: A condition that checks if a datetime is next year.
    """
    return lambda d: __check_is_year(d, 1)


def next_year_utc():
    """
    A condition that checks if a datetime is next year calculating in UTC (use without
    parenthesis in your Stream).
    :return: A condition that checks if a datetime is next year.
    """
    return lambda d: __check_is_year(d, 1, tz=__timezone.utc)


def __check_is_year(d: Union[__datetime, __date], offset: int = 0, tz: __timezone = None):
    """
    A condition that checks if a datetime is a specific year also supporting
    UTC timezone and offsets.
    :param d: The datetime to check against.
    :param offset: The offset to check against.
    """
    return __datetime.now(tz).date().year + offset == d.astimezone(tz).date().year if \
        isinstance(d, __datetime) else __datetime.now(tz).date().year + offset == d.year


def reduce_to_valid_range(value, range_val) -> int:
    result = value - (range_val * (value // range_val))
    return range_val if result == 0 else result
