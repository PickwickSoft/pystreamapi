from abc import abstractmethod, ABC
from collections import Counter
from typing import Union

from pystreamapi._streams.__base_stream import BaseStream


class NumericBaseStream(BaseStream, ABC):

    @abstractmethod
    def mean(self) -> Union[float, int]:
        """
        Calculates the mean of a numerical Stream
        :return: The mean, can be int or float
        """

    def median(self) -> Union[float, int, None]:
        self._trigger_exec()
        return self.__median(self._source)

    @staticmethod
    def __median(source) -> Union[float, int, None]:
        source = sorted(source)
        if not source:
            return None
        midpoint = len(source) // 2
        if len(source) % 2 == 0:
            return (source[midpoint] + source[midpoint - 1]) / 2
        return source[midpoint]

    def first_quartile(self) -> Union[float, int, None]:
        self._trigger_exec()
        self._source = sorted(self._source)
        return self.__median(self._source[:(len(self._source)) // 2])

    def third_quartile(self) -> Union[float, int, None]:
        self._trigger_exec()
        self._source = sorted(self._source)
        return self.__median(self._source[(len(self._source) + 1) // 2:])

    def mode(self) -> Union[list[Union[int, float]], None]:
        self._trigger_exec()
        frequency = Counter(self._source)
        if not frequency:
            return None
        max_frequency = max(frequency.values())
        return [number for number, count in frequency.items() if count == max_frequency]

    def range(self) -> Union[float, int, None]:
        self._trigger_exec()
        return max(self._source) - min(self._source) if len(self._source) > 0 else None

    def interquartile_range(self) -> Union[float, int, None]:
        self._trigger_exec()
        return self.third_quartile() - self.first_quartile() if len(self._source) > 0 else None
