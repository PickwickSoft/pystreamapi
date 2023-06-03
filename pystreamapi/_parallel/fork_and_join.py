import os

from functools import reduce
from typing import Callable, Any

from joblib import Parallel, delayed


class Parallelizer:
    r"""
    Implementation of the fork-and-join technology.

    A given list gets split into multiple sublists,
    processed and afterward combined into a single one.

    Eg.: [1, 2, 3, 4, 5, 6] should be reduced using `sum()`\n
    Split: [[1, 2], [3, 4], [5, 6]]\n
    Filter/Reduce: [[3], [7], [11]]\n
    Combine: 21
    """

    def __init__(self):
        self.__src = None

    def set_source(self, src: list):
        """Set the source list
        :param src: The source list
        """
        self.__src = src

    def filter(self, function):
        """Parallel filter function"""
        parts = self.fork()
        result = self.__run_job_in_parallel(parts, self.__filter, function)
        return [item for sublist in result for item in sublist]

    def reduce(self, function: Callable[[Any, Any], Any]):
        """Parallel reduce function using functools.reduce behind"""
        if len(self.__src) < 2:
            return self.__src
        parts = self.fork(min_nr_items=2)
        result = self.__run_job_in_parallel(parts, reduce, function)
        return reduce(function, result)

    @staticmethod
    def __filter(function, src):
        """Filter function used in the fork-and-join technology"""
        return [element for element in src if function(element)]

    def fork(self, min_nr_items=1):
        """
        Split the source list into multiple sublists.
        The number of sublists is calculated based on the number of CPU cores.
        :param min_nr_items: The minimum number of items per sublist
        :return: A list of sublists
        """
        if min_nr_items < 1:
            raise ValueError("There cannot be less than one element per list")
        if len(self.__src) == 0:
            return self.__src
        nr_of_parts = self.__calculate_number_of_parts(min_nr_items)
        return self.__split_list(nr_of_parts)

    def __split_list(self, nr_of_parts):
        """Split the source list into multiple sublists"""
        k, m = divmod(len(self.__src), nr_of_parts)
        return [
            self.__src[i * k + min(i, m) : (i + 1) * k + min(i + 1, m)]
            for i in range(nr_of_parts)
        ]

    def __calculate_number_of_parts(self, min_nr_items=1):
        """Calculate the number of sublists"""
        if len(self.__src) < min_nr_items:
            return len(self.__src)
        if (len(self.__src) / min_nr_items) < os.cpu_count():
            return round(len(self.__src) / min_nr_items)
        return os.cpu_count() - 2 if os.cpu_count() > 2 else os.cpu_count()

    @staticmethod
    def __run_job_in_parallel(src, operation, op_function):
        """Run the operation in parallel"""
        return Parallel(n_jobs=-1, prefer="processes")(delayed(operation)(op_function, part)
                                                       for part in src)
