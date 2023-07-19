# pylint: disable=protected-access
from pystreamapi._streams.error.__error import ErrorHandler, _sentinel


def dropwhile(predicate, iterable, handler: ErrorHandler=None):
    """
    Drop items from the iterable while predicate(item) is true.
    Afterward, return every element until the iterable is exhausted.
    """
    it = iter(iterable)
    for x in it:
        if handler is not None:
            res = handler._one(mapper=predicate, item=x)
        else:
            res = predicate(x)
        if not res and res is not _sentinel:
            yield x
            break
    yield from it


_initial_missing = object()


def reduce(function, sequence, initial=_initial_missing, handler: ErrorHandler=None):
    """
    Apply a function of two arguments cumulatively to the items of a sequence
    or iterable, from left to right, to reduce the iterable to a single
    value.  For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
    ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
    of the iterable in the calculation, and serves as a default when the
    iterable is empty.
    """
    it = iter(sequence)

    if initial is _initial_missing:
        try:
            value = next(it)
        except StopIteration:
            raise TypeError(
                "reduce() of empty iterable with no initial value") from None
    else:
        value = initial

    for element in it:
        if handler is not None:
            new_value = handler._one(mapper=lambda x, val=value: function(val, x), item=element)
            if new_value is not _sentinel:
                value = new_value
        else:
            value = function(value, element)

    return value
