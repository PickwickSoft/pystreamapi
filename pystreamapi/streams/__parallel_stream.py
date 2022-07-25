from typing import Callable, Any, Iterable

import pystreamapi.streams.basestream as stream
from pystreamapi.lazy.process import Process
from pystreamapi.parallel.parallelize import parallelize


class ParallelStream(stream.BaseStream):

    def __init__(self, source: Iterable):
        super().__init__(source)

    def filter(self, function: Callable[[Any], bool]):
        self._queue.append(Process(self.__filter, function))
        return self

    def __filter(self, function: Callable[[Any], bool]):
        self._source = [element for element in parallelize(self._source) if function(element)]

    def map(self, function: Callable[[Any], bool]):
        self._queue.append(Process(self.__map, function))
        return self

    def __map(self, function: Callable[[Any], Any]):
        self._source = [function(element) for element in parallelize(self._source)]

    def peek(self, function: Callable):
        self._queue.append(Process(self.__peek, function))
        return self

    def __peek(self, function: Callable):
        for element in parallelize(self._source):
            function(element)

    def for_each(self, function: Callable):
        self._trigger_exec()
        for element in parallelize(self._source):
            function(element)
