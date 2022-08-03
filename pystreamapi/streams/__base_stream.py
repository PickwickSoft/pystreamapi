import itertools
from abc import abstractmethod
from builtins import reversed
from typing import Iterable, Callable, Any, TypeVar

from optional import Optional

from pystreamapi.lazy.process import Process
from pystreamapi.lazy.queue import ProcessQueue

_K = TypeVar('_K')


class BaseStream:

    def __init__(self, source: Iterable):
        self._source = source
        self._queue = ProcessQueue()

    def __iter__(self):
        self._trigger_exec()
        return iter(self._source)

    def __reversed__(self):
        self.__reversed()
        return self

    @abstractmethod
    def filter(self, function: Callable[[Any], bool]):
        pass

    @abstractmethod
    def map(self, function: Callable[[Any], Any]):
        pass

    @abstractmethod
    def map_to_int(self):
        pass

    @abstractmethod
    def map_to_str(self):
        pass

    @abstractmethod
    def flat_map(self, function: Callable):
        pass

    @abstractmethod
    def peek(self, function: Callable):
        pass

    def limit(self, limit: int):
        self._queue.append(Process(self.__limit, limit))
        return self

    def __limit(self, limit: int):
        self._source = self._source[:limit]

    def skip(self, count: int):
        self._queue.append(Process(self.__skip, count))
        return self

    def __skip(self, count: int):
        self._source = self._source[count:]

    def distinct(self):
        self._queue.append(Process(self.__distinct))
        return self

    def __distinct(self):
        self._source = list(set(self._source))

    def sorted(self):
        self._queue.append(Process(self.__sorted))
        return self

    def __sorted(self):
        self._source = sorted(self._source)

    def reversed(self):
        self._queue.append(Process(self.__reversed))
        return self

    def __reversed(self):
        try:
            self._source = reversed(self._source)
        except TypeError:
            self._source = reversed(list(self._source))

    def drop_while(self, function: Callable[[Any], bool]):
        self._queue.append(Process(self.__drop_while, function))
        return self

    def __drop_while(self, function: Callable[[Any], bool]):
        self._source = list(itertools.dropwhile(function, self._source))

    def take_while(self, function: Callable[[Any], bool]):
        self._queue.append(Process(self.__take_while, function))
        return self

    def __take_while(self, function: Callable[[Any], bool]):
        self._source = list(itertools.takewhile(function, self._source))

    @abstractmethod
    def find_any(self) -> Optional:
        pass

    @abstractmethod
    def for_each(self, function: Callable):
        pass

    @abstractmethod
    def reduce(self, function: Callable[[Any, Any], Any], identity):
        pass

    @abstractmethod
    def all_match(self, function: Callable[[Any], bool]):
        pass

    def any_match(self, function: Callable[[Any], bool]):
        self._trigger_exec()
        return any(function(element) for element in self._source)

    def none_match(self, function: Callable[[Any], bool]):
        self._trigger_exec()
        return not any(function(element) for element in self._source)

    def min(self):
        self._trigger_exec()
        if len(self._source) > 0:
            return Optional.of(min(self._source))
        return Optional.empty()

    def max(self):
        self._trigger_exec()
        if len(self._source) > 0:
            return Optional.of(max(self._source))
        return Optional.empty()

    def find_first(self):
        self._trigger_exec()
        if len(self._source) > 0:
            return Optional.of(self._source[0])
        return Optional.empty()

    def to_list(self):
        self._trigger_exec()
        return list(self._source)

    def to_tuple(self):
        self._trigger_exec()
        return tuple(self._source)

    def to_set(self):
        self._trigger_exec()
        return set(self._source)

    def count(self):
        self._trigger_exec()
        return len(self._source)

    def _trigger_exec(self):
        self._queue.execute_all()
