from typing import Union

from pystreamapi._streams.__sequential_stream import SequentialStream
from pystreamapi._streams.numeric.__numeric_base_stream import NumericBaseStream


class SequentialNumericStream(NumericBaseStream, SequentialStream):

    def mean(self) -> Union[float, int, None]:
        self._trigger_exec()
        return sum(self._source) / len(self._source) if len(self._source) > 0 else None
