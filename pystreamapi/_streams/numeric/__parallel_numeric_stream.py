from typing import Union

from pystreamapi._streams.__parallel_stream import ParallelStream
from pystreamapi._streams.numeric.__numeric_base_stream import NumericBaseStream


class ParallelNumericStream(NumericBaseStream, ParallelStream):
    """Numeric Stream with parallel implementation"""

    def mean(self) -> Union[float, int, None]:
        """Calculates mean of values"""
        self._trigger_exec()
        return self.__sum() / len(self._source) if len(self._source) > 0 else None

    def sum(self) -> Union[float, int, None]:
        """Calculates the sum of values"""
        self._trigger_exec()
        _sum = self.__sum()
        return 0 if _sum == [] else _sum

    def __sum(self):
        """Parallel sum method"""
        self._set_parallelizer_src()
        return self._parallelizer.reduce(lambda x, y: x + y)