from abc import abstractmethod
from functools import reduce
from typing import Iterable, Callable, Any

from pystreamapi.lazy.queue import ProcessQueue


class BaseStream:

    def __init__(self, source: Iterable):
        self._source = list(source)
        self._queue = ProcessQueue()

    @abstractmethod
    def filter(self, function: Callable[[Any], bool]):
        pass

    @abstractmethod
    def __filter(self, function: Callable[[Any], bool]):
        pass

    @abstractmethod
    def map(self, function: Callable[[Any], bool]):
        pass

    @abstractmethod
    def __map(self, function: Callable[[Any], Any]):
        pass

    @abstractmethod
    def peek(self, function: Callable):
        pass

    @abstractmethod
    def __peek(self, function: Callable):
        pass

    @abstractmethod
    def for_each(self, function: Callable):
        pass

    def reduce(self, function: Callable):
        self._trigger_exec()
        return reduce(function, self._source)

    def sorted(self):
        self._trigger_exec()
        self._source.sort()
        return self

    def to_list(self):
        self._trigger_exec()
        return self._source

    def count(self):
        self._trigger_exec()
        return len(self._source)

    def _trigger_exec(self):
        self._queue.execute_all()
