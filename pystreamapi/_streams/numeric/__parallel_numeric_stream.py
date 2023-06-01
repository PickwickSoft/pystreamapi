from typing import Union

from pystreamapi._streams.__parallel_stream import ParallelStream
from pystreamapi._streams.numeric.__numeric_base_stream import NumericBaseStream


class ParallelNumericStream(NumericBaseStream, ParallelStream):

    def mean(self) -> Union[float, int, None]:
        self._trigger_exec()
        return self.__sum() / len(self._source) if len(self._source) > 0 else None

    def __sum(self):
        self._set_parallelizer_src()
        return self.parallelizer.reduce(lambda x, y: x + y)
