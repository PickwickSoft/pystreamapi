from abc import abstractmethod, ABC
from collections import Counter
from typing import Union

from pystreamapi._streams.__base_stream import BaseStream, terminal


class NumericBaseStream(BaseStream, ABC):
    """
    This stream extends the capabilities of the default stream by introducing numerical operations.
    It is designed specifically for use with numerical data sources and can only be applied
    to such data.
    """

    @terminal
    def interquartile_range(self) -> Union[float, int, None]:
        """
        Calculates the iterquartile range of a numerical Stream
        :return: The iterquartile range, can be int or float
        """
        return self._interquartile_range()

    def _interquartile_range(self):
        """Implementation of the interquartile range calculation"""
        return self._third_quartile() - self._first_quartile() if len(self._source) > 0 else None

    @terminal
    def first_quartile(self) -> Union[float, int, None]:
        """
        Calculates the first quartile of a numerical Stream
        :return: The first quartile, can be int or float
        """
        return self._first_quartile()

    def _first_quartile(self):
        """Implementation of the first quartile calculation"""
        self._source = sorted(self._source)
        return self.__median(self._source[:(len(self._source)) // 2])

    @abstractmethod
    @terminal
    def mean(self) -> Union[float, int]:
        """
        Calculates the mean of a numerical Stream
        :return: The mean, can be int or float
        """

    @terminal
    def median(self) -> Union[float, int, None]:
        """
        Calculates the median of a numerical Stream
        :return: The median, can be int or float
        """
        return self.__median(self._source)

    @staticmethod
    def __median(source) -> Union[float, int, None]:
        """Calculates the median of a numerical Stream"""
        source = sorted(source)
        if not source:
            return None
        midpoint = len(source) // 2
        if len(source) % 2 == 0:
            return (source[midpoint] + source[midpoint - 1]) / 2
        return source[midpoint]

    @terminal
    def mode(self) -> Union[list[Union[int, float]], None]:
        """
        Calculates the mode/modes (most frequently occurring element/elements) of a numerical Stream
        :return: The mode, can be int or float
        """
        frequency = Counter(self._source)
        if not frequency:
            return None
        max_frequency = max(frequency.values())
        return [number for number, count in frequency.items() if count == max_frequency]

    @terminal
    def range(self) -> Union[float, int, None]:
        """
        Calculates the range of a numerical Stream
        :return: The range, can be int or float
        """
        return max(self._source) - min(self._source) if len(self._source) > 0 else None

    @abstractmethod
    @terminal
    def sum(self) -> Union[float, int, None]:
        """
        Calculates the sum of all items of a numerical stream
        :return: The sum, can be int or float
        """

    @terminal
    def third_quartile(self) -> Union[float, int, None]:
        """
        Calculates the third quartile of a numerical Stream
        :return: The third quartile, can be int or float
        """
        return self._third_quartile()

    def _third_quartile(self):
        """Implementation of the third quartile calculation"""
        self._source = sorted(self._source)
        return self.__median(self._source[(len(self._source) + 1) // 2:])
