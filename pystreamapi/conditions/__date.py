from datetime import datetime as __datetime, timedelta as __timedelta, timezone as __timezone


def before(d: __datetime):
    return lambda y: y < d


def after(d: __datetime):
    return lambda y: y > d


def before_or_equal(d: __datetime):
    return lambda y: y <= d


def after_or_equal(d: __datetime):
    return lambda y: y >= d


def equal_to(d: __datetime):
    return lambda y: y == d


def not_equal_to(d: __datetime):
    return lambda y: y != d


def between(d: __datetime, y: __datetime):
    return lambda z: d <= z <= y


def not_between(d: __datetime, y: __datetime):
    return lambda z: not (d <= z <= y)


def between_or_equal(d: __datetime, y: __datetime):
    return lambda z: d <= z <= y


def not_between_or_equal(d: __datetime, y: __datetime):
    return lambda z: not (d <= z <= y)


def today(d: __datetime):
    return __datetime.now().date() == d.date()


def today_utc(d: __datetime):
    return __datetime.now(__timezone.utc).date() == d.astimezone(__timezone.utc).date()


def yesterday(d: __datetime):
    return __datetime.now().date() - __timedelta(days=1) == d.date()


def yesterday_utc(d: __datetime):
    return __datetime.now(__timezone.utc).date() - __timedelta(days=1) == d.astimezone(
        __timezone.utc).date()


def tomorrow(d: __datetime):
    return __datetime.now().date() + __timedelta(days=1) == d.date()


def tomorrow_utc(d: __datetime):
    return __datetime.now(__timezone.utc).date() + __timedelta(days=1) == d.astimezone(
        __timezone.utc).date()


def this_week(d: __datetime):
    return __datetime.now().date().isocalendar()[1] == d.date().isocalendar()[1]


def this_week_utc(d: __datetime):
    return __datetime.now(__timezone.utc).date().isocalendar()[1] == \
        d.astimezone(__timezone.utc).date().isocalendar()[1]


def last_week(d: __datetime):
    return __datetime.now().date().isocalendar()[1] - 1 == d.date().isocalendar()[1]


def last_week_utc(d: __datetime):
    return __datetime.now(__timezone.utc).date().isocalendar()[1] - 1 == \
        d.astimezone(__timezone.utc).date().isocalendar()[1]


def next_week(d: __datetime):
    return __datetime.now().date().isocalendar()[1] + 1 == d.date().isocalendar()[1]


def next_week_utc(d: __datetime):
    return __datetime.now(__timezone.utc).date().isocalendar()[1] + 1 == \
        d.astimezone(__timezone.utc).date().isocalendar()[1]


def this_month(d: __datetime):
    return __check_is_month(d)


def this_month_utc(d: __datetime):
    return __check_is_month(d, tz=__timezone.utc)


def last_month(d: __datetime):
    return __check_is_month(d, -1)


def last_month_utc(d: __datetime):
    return __check_is_month(d, -1, tz=__timezone.utc)


def next_month(d: __datetime):
    return __check_is_month(d, 1)


def next_month_utc(d: __datetime):
    return __check_is_month(d, 1, tz=__timezone.utc)


def __check_is_month(d: __datetime, offset: int = 0, tz: __timezone = None):
    return __datetime.now(tz).date().month + offset == d.astimezone(tz).date().month


def this_year(d: __datetime):
    return __check_is_year(d)


def this_year_utc(d: __datetime):
    return __check_is_year(d, tz=__timezone.utc)


def last_year(d: __datetime):
    return __check_is_year(d, -1)


def last_year_utc(d: __datetime):
    return __check_is_year(d, -1, tz=__timezone.utc)


def next_year(d: __datetime):
    return __check_is_year(d, 1)


def next_year_utc(d: __datetime):
    return __check_is_year(d, 1, tz=__timezone.utc)


def __check_is_year(d: __datetime, offset: int = 0, tz: __timezone = None):
    return __datetime.now(tz).date().year + offset == d.astimezone(tz).date().year
