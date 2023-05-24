from datetime import datetime as __datetime, timedelta as __timedelta, timezone as __timezone


def before(d: __datetime):
    """
    Returns a condition that checks if a datetime is before a given datetime.
    :param d: The datetime to check against.
    :return: A condition that checks if a datetime is before a given datetime.
    """
    return lambda y: y < d


def after(d: __datetime):
    """
    Returns a condition that checks if a datetime is after a given datetime.
    :param d: The datetime to check against.
    :return: A condition that checks if a datetime is after a given datetime.
    """
    return lambda y: y > d


def before_or_equal(d: __datetime):
    """
    Returns a condition that checks if a datetime is before or equal to a given datetime.
    :param d: The datetime to check against.
    :return: A condition that checks if a datetime is before or equal to a given datetime.
    """
    return lambda y: y <= d


def after_or_equal(d: __datetime):
    """
    Returns a condition that checks if a datetime is after or equal to a given datetime.
    :param d: The datetime to check against.
    :return: A condition that checks if a datetime is after or equal to a given datetime.
    """
    return lambda y: y >= d


def between_or_equal(d: __datetime, y: __datetime):
    """
    Returns a condition that checks if a datetime is between or equal to two given datetimes.
    :param d: The datetime to check against.
    :param y: The datetime to check against.
    :return: A condition that checks if a datetime is between or equal to two given datetimes.
    """
    return lambda z: d <= z <= y


def not_between_or_equal(d: __datetime, y: __datetime):
    """
    Returns a condition that checks if a datetime is not between or equal to two given datetimes.
    :param d: The datetime to check against.
    :param y: The datetime to check against.
    :return: A condition that checks if a datetime is not between or equal to two given datetimes.
    """
    return lambda z: not d <= z <= y


def today(d: __datetime):
    """
    The condition that checks if a datetime is today (use without parenthesis in your Stream).
    :param d: The datetime to check against.
    :return: A condition that checks if a datetime is today.
    """
    return __datetime.now().date() == d.date()


def today_utc(d: __datetime):
    """
    The condition that checks if a datetime is today calculating in UTC (use without parenthesis
    in your Stream).
    :param d: The datetime to check against.
    :return: A condition that checks if a datetime is today.
    """
    return __datetime.now(__timezone.utc).date() == d.astimezone(__timezone.utc).date()


def yesterday(d: __datetime):
    """
    The condition that checks if a datetime is yesterday (use without parenthesis in your Stream).
    :param d: The datetime to check against.
    :return: A condition that checks if a datetime is yesterday.
    """
    return __datetime.now().date() - __timedelta(days=1) == d.date()


def yesterday_utc(d: __datetime):
    """
    The condition that checks if a datetime is yesterday calculating in UTC (use without
    parenthesis in your Stream).
    :param d: The datetime to check against.
    :return: A condition that checks if a datetime is yesterday.
    """
    return __datetime.now(__timezone.utc).date() - __timedelta(days=1) == d.astimezone(
        __timezone.utc).date()


def tomorrow(d: __datetime):
    """
    A condition that checks if a datetime is tomorrow (use without parenthesis in your Stream).
    :param d: The datetime to check against.
    :return: A condition that checks if a datetime is tomorrow.
    """
    return __datetime.now().date() + __timedelta(days=1) == d.date()


def tomorrow_utc(d: __datetime):
    """
    A condition that checks if a datetime is tomorrow calculating in UTC (use without parenthesis
    in your Stream).
    :param d: The datetime to check against.
    :return: A condition that checks if a datetime is tomorrow.
    """
    return __datetime.now(__timezone.utc).date() + __timedelta(days=1) == d.astimezone(
        __timezone.utc).date()


def this_week(d: __datetime):
    """
    A condition that checks if a datetime is this week (use without parenthesis in your Stream).
    :param d: The datetime to check against.
    :return: A condition that checks if a datetime is this week.
    """
    return __datetime.now().date().isocalendar()[1] == d.date().isocalendar()[1]


def this_week_utc(d: __datetime):
    """
    A condition that checks if a datetime is this week calculating in UTC (use without
    parenthesis in your Stream).
    :param d: The datetime to check against.
    :return: A condition that checks if a datetime is this week.
    """
    return __datetime.now(__timezone.utc).date().isocalendar()[1] == \
        d.astimezone(__timezone.utc).date().isocalendar()[1]


def last_week(d: __datetime):
    """
    A condition that checks if a datetime is last week (use without parenthesis in your Stream).
    :param d: The datetime to check against.
    :return: A condition that checks if a datetime is last week.
    """
    return __datetime.now().date().isocalendar()[1] - 1 == d.date().isocalendar()[1]


def last_week_utc(d: __datetime):
    """
    A condition that checks if a datetime is last week calculating in UTC (use without
    parenthesis in your Stream).
    :param d: The datetime to check against.
    :return: A condition that checks if a datetime is last week.
    """
    return __datetime.now(__timezone.utc).date().isocalendar()[1] - 1 == \
        d.astimezone(__timezone.utc).date().isocalendar()[1]


def next_week(d: __datetime):
    """
    A condition that checks if a datetime is next week (use without parenthesis in your Stream).
    :param d: The datetime to check against.
    :return: A condition that checks if a datetime is next week.
    """
    return __datetime.now().date().isocalendar()[1] + 1 == d.date().isocalendar()[1]


def next_week_utc(d: __datetime):
    """
    A condition that checks if a datetime is next week calculating in UTC (use without
    parenthesis in your Stream).
    :param d: The datetime to check against.
    :return: A condition that checks if a datetime is next week.
    """
    return __datetime.now(__timezone.utc).date().isocalendar()[1] + 1 == \
        d.astimezone(__timezone.utc).date().isocalendar()[1]


def this_month(d: __datetime):
    """
    A condition that checks if a datetime is this month (use without parenthesis in your Stream).
    :param d: The datetime to check against.
    :return: A condition that checks if a datetime is this month.
    """
    return __check_is_month(d)


def this_month_utc(d: __datetime):
    """
    A condition that checks if a datetime is this month calculating in UTC (use without
    parenthesis in your Stream).
    :param d: The datetime to check against.
    :return: A condition that checks if a datetime is this month.
    """
    return __check_is_month(d, tz=__timezone.utc)


def last_month(d: __datetime):
    """
    A condition that checks if a datetime is last month (use without parenthesis in your Stream).
    :param d: The datetime to check against.
    :return: A condition that checks if a datetime is last month.
    """
    return __check_is_month(d, -1)


def last_month_utc(d: __datetime):
    """
    A condition that checks if a datetime is last month calculating in UTC (use without
    parenthesis in your Stream).
    :param d: The datetime to check against.
    :return: A condition that checks if a datetime is last month.
    """
    return __check_is_month(d, -1, tz=__timezone.utc)


def next_month(d: __datetime):
    """
    A condition that checks if a datetime is next month (use without parenthesis in your Stream).
    :param d: The datetime to check against.
    :return: A condition that checks if a datetime is next month.
    """
    return __check_is_month(d, 1)


def next_month_utc(d: __datetime):
    """
    A condition that checks if a datetime is next month calculating in UTC (use without
    parenthesis in your Stream).
    :param d: The datetime to check against.
    :return: A condition that checks if a datetime is next month.
    """
    return __check_is_month(d, 1, tz=__timezone.utc)


def __check_is_month(d: __datetime, offset: int = 0, tz: __timezone = None):
    """
    The actual function that checks if a datetime is a specific month also supporting
    UTC timezone and offsets.
    :param d: The datetime to check against.
    :param offset: The offset to check against.
    :param tz: The timezone to check against.
    """
    return __datetime.now(tz).date().month + offset == d.astimezone(tz).date().month


def this_year(d: __datetime):
    """
    A condition that checks if a datetime is this year (use without parenthesis in your Stream).
    :param d: The datetime to check against.
    :return: A condition that checks if a datetime is this year.
    """
    return __check_is_year(d)


def this_year_utc(d: __datetime):
    """
    A condition that checks if a datetime is this year calculating in UTC (use without
    parenthesis in your Stream).
    :param d: The datetime to check against.
    """
    return __check_is_year(d, tz=__timezone.utc)


def last_year(d: __datetime):
    """
    A condition that checks if a datetime is last year (use without parenthesis in your Stream).
    :param d: The datetime to check against.
    :return: A condition that checks if a datetime is last year.
    """
    return __check_is_year(d, -1)


def last_year_utc(d: __datetime):
    """
    A condition that checks if a datetime is last year calculating in UTC (use without
    parenthesis in your Stream).
    :param d: The datetime to check against.
    :return: A condition that checks if a datetime is last year.
    """
    return __check_is_year(d, -1, tz=__timezone.utc)


def next_year(d: __datetime):
    """
    A condition that checks if a datetime is next year (use without parenthesis in your Stream).
    :param d: The datetime to check against.
    :return: A condition that checks if a datetime is next year.
    """
    return __check_is_year(d, 1)


def next_year_utc(d: __datetime):
    """
    A condition that checks if a datetime is next year calculating in UTC (use without
    parenthesis in your Stream).
    :param d: The datetime to check against.
    :return: A condition that checks if a datetime is next year.
    """
    return __check_is_year(d, 1, tz=__timezone.utc)


def __check_is_year(d: __datetime, offset: int = 0, tz: __timezone = None):
    """
    A condition that checks if a datetime is a specific year also supporting
    UTC timezone and offsets.
    :param d: The datetime to check against.
    :param offset: The offset to check against.
    """
    return __datetime.now(tz).date().year + offset == d.astimezone(tz).date().year