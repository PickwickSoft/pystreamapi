from typing import Callable, Any, Iterable
from optional import Optional

import pystreamapi.streams.basestream as stream
from pystreamapi.lazy.process import Process


class SequentialStream(stream.BaseStream):

    def filter(self, function: Callable[[Any], bool]):
        self._queue.append(Process(self.__filter, function))
        return self

    def __filter(self, function: Callable[[Any], bool]):
        self._source = [element for element in self._source if function(element)]

    def map(self, function: Callable[[Any], Any]):
        self._queue.append(Process(self.__map, function))
        return self

    def __map(self, function: Callable[[Any], Any]):
        self._source = [function(element) for element in self._source]

    def map_to_int(self):
        self._queue.append(Process(self.__map_to_int))
        return self

    def __map_to_int(self):
        self.__map(int)

    def map_to_str(self):
        self._queue.append(Process(self.__map_to_str))
        return self

    def __map_to_str(self):
        self.__map(str)

    def flat_map(self, function: Callable[[Any], stream.BaseStream]):
        self._queue.append(Process(self.__flat_map, function))
        return self

    def __flat_map(self, function: Callable[[Any], stream.BaseStream]):
        new_src = []
        for element in [function(element) for element in self._source]:
            new_src.extend(element.to_list())
        self._source = new_src

    def peek(self, function: Callable):
        self._queue.append(Process(self.__peek, function))
        return self

    def __peek(self, function: Callable):
        for element in self._source:
            function(element)

    def all_match(self, function: Callable[[Any], bool]):
        self._trigger_exec()
        return all(function(element) for element in self._source)

    def find_any(self):
        self._trigger_exec()
        if len(self._source) > 0:
            return Optional.of(self._source[0])
        return Optional.empty()

    def for_each(self, function: Callable):
        self._trigger_exec()
        for element in self._source:
            function(element)
