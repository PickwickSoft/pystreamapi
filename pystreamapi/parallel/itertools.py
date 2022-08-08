import os
from typing import Callable, Any
from functools import reduce as iter_reduce
from joblib import Parallel, delayed


def pfilter(src, function):
    """Filter in parallel using parallelism"""
    if len(src) < 1:
        return src
    cpu_nr = os.cpu_count() - 2 if os.cpu_count() > 2 else os.cpu_count()
    parts = list(__split(src, cpu_nr))
    res = Parallel(n_jobs=-1)(delayed(__filter)(part, function) for part in parts)
    new = []
    for element in res:
        new.extend(element)
    return new


def __filter(src, function):
    return [element for element in src if function(element)]


def reduce(function: Callable[[Any, Any], Any], source: list):
    """Parallel reduce function using functools.reduce behind"""
    if len(source) < 2:
        return source
    cpu_nr = os.cpu_count()
    parts = list(__split_to_two(source, cpu_nr))
    res = Parallel(n_jobs=-1)(delayed(iter_reduce)(function, lst) for lst in parts)
    return iter_reduce(function, res)


def __split_to_two(lst, n):
    if (len(lst) // 2) < n:
        n = len(lst) // 2
    k, m = divmod(len(lst), n)
    return (lst[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))


def __split(lst, n):
    k, m = divmod(len(lst), n)
    return (lst[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))
