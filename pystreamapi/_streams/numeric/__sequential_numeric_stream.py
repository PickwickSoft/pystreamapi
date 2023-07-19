from typing import Union

from pystreamapi._streams.__base_stream import terminal
from pystreamapi._streams.__sequential_stream import SequentialStream
from pystreamapi._streams.numeric.__numeric_base_stream import NumericBaseStream


class SequentialNumericStream(NumericBaseStream, SequentialStream):
    """Numeric Stream with sequential implementation"""

    @terminal
    def mean(self) -> Union[float, int, None]:
        """Calculates mean of values"""
        return sum(self._source) / len(self._source) if len(self._source) > 0 else None

    @terminal
    def sum(self) -> Union[float, int, None]:
        """Calculates the sum of values"""
        return sum(self._source)
