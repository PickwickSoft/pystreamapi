from abc import abstractmethod
from functools import reduce
from typing import Iterable, Callable, Any

from optional import Optional

from pystreamapi.lazy.queue import ProcessQueue

_identity_missing = object()


class BaseStream:

    def __init__(self, source: Iterable):
        self._source = list(source)
        self._queue = ProcessQueue()

    @abstractmethod
    def filter(self, function: Callable[[Any], bool]):
        pass

    @abstractmethod
    def map(self, function: Callable[[Any], bool]):
        pass

    @abstractmethod
    def peek(self, function: Callable):
        pass

    @abstractmethod
    def find_any(self) -> Optional:
        pass

    @abstractmethod
    def for_each(self, function: Callable):
        pass

    def reduce(self, function: Callable, identity=_identity_missing):
        self._trigger_exec()
        if len(self._source) > 0:
            if identity is not _identity_missing:
                return reduce(function, self._source)
            return Optional.of(reduce(function, self._source))
        elif identity is not _identity_missing:
            return identity
        else:
            Optional.empty()

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

    def sorted(self):
        self._trigger_exec()
        self._source.sort()
        return self

    def to_list(self):
        self._trigger_exec()
        return self._source

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
