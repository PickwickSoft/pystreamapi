import itertools
from abc import abstractmethod
from builtins import reversed
from typing import Iterable, Callable, Any, TypeVar, Iterator

from optional import Optional

from pystreamapi.lazy.process import Process
from pystreamapi.lazy.queue import ProcessQueue

_K = TypeVar('_K')
_V = TypeVar('_V')


class BaseStream(Iterable[_K]):
    """
    A sequence of elements supporting sequential and parallel aggregate operations.

    To perform a computation, stream operations are composed into a stream pipeline. A stream
    pipeline consists of a source (which might be an array, a collection, a generator function,
    an I/O channel, etc.), zero or more intermediate operations (which transform a stream into
    another stream, such as filter(Predicate)), and a terminal operation (which produces a result
    or side effect, such as count() or forEach(Consumer)). Streams are lazy; computation on the
    source data is only performed when the terminal operation is initiated, and source elements
    are consumed only as needed.
    """

    def __init__(self, source: Iterable[_K]):
        self._source = source
        self._queue = ProcessQueue()

    def __iter__(self) -> Iterator[_K]:
        self._trigger_exec()
        return iter(self._source)

    def __reversed__(self):
        self.__reversed()
        return self

    @classmethod
    def concat(cls, *streams: "BaseStream[_K]"):
        """
        Creates a lazily concatenated stream whose elements are all the elements of the first stream
        followed by all the elements of the other streams.

        :param streams: The streams to concatenate
        :return: The concatenated stream
        """
        return cls(itertools.chain(*list(streams)))

    @abstractmethod
    def filter(self, predicate: Callable[[_K], bool]):
        """
        Returns a stream consisting of the elements of this stream that match the given predicate.

        :param predicate:
        """
        return self

    @abstractmethod
    def map(self, mapper: Callable[[_K], _V]) -> 'BaseStream[_V]':
        """
        Returns a stream consisting of the results of applying the given function to the elements
        of this stream.

        :param mapper:
        """
        return self

    @abstractmethod
    def map_to_int(self):
        """
        Returns a stream consisting of the results of converting the elements of this stream to
        integers.
        """
        return self

    @abstractmethod
    def map_to_str(self):
        """
        Returns a stream consisting of the results of converting the elements of this stream to
        strings.
        """
        return self

    @abstractmethod
    def flat_map(self, predicate: Callable[[_K], Iterable[_V]]):
        """
        Returns a stream consisting of the results of replacing each element of this stream with
        the contents of a mapped stream produced by applying the provided mapping function to
        each element.

        :param predicate:
        """
        return self

    @abstractmethod
    def peek(self, action: Callable):
        """
        Returns a stream consisting of the elements of this stream, additionally performing the
        provided action on each element as elements are consumed from the resulting stream.

        :param action:
        """
        return self

    def limit(self, max_size: int):
        """
        Returns a stream consisting of the elements of this stream, truncated to be no longer
        than maxSize in length.

        :param max_size:
        """
        self._queue.append(Process(self.__limit, max_size))
        return self

    def __limit(self, max_size: int):
        self._source = itertools.islice(self._source, max_size)

    def skip(self, n: int):
        """
        Returns a stream consisting of the remaining elements of this stream after discarding the
        first n elements of the stream.

        :param n:
        """
        self._queue.append(Process(self.__skip, n))
        return self

    def __skip(self, n: int):
        self._source = self._source[n:]

    def distinct(self):
        """Returns a stream consisting of the distinct elements of this stream."""
        self._queue.append(Process(self.__distinct))
        return self

    def __distinct(self):
        self._source = list(set(self._source))

    def sorted(self):
        """
        Returns a stream consisting of the elements of this stream, sorted according to natural
        order.
        """
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

    def drop_while(self, predicate: Callable[[_K], bool]):
        """
        Returns, if this stream is ordered, a stream consisting of the remaining elements of this
        stream after dropping the longest prefix of elements that match the given predicate.

        :param predicate:
        """
        self._queue.append(Process(self.__drop_while, predicate))
        return self

    def __drop_while(self, predicate: Callable[[Any], bool]):
        self._source = list(itertools.dropwhile(predicate, self._source))

    def take_while(self, predicate: Callable[[_K], bool]):
        """
        Returns, if this stream is ordered, a stream consisting of the longest prefix of elements
        taken from this stream that match the given predicate.

        :param predicate:
        """
        self._queue.append(Process(self.__take_while, predicate))
        return self

    def __take_while(self, predicate: Callable[[Any], bool]):
        self._source = list(itertools.takewhile(predicate, self._source))

    @abstractmethod
    def find_any(self) -> Optional:
        """
        Returns an Optional describing some element of the stream, or an empty Optional if the
        stream is empty.
        """

    @abstractmethod
    def for_each(self, predicate: Callable):
        """
        Performs an action for each element of this stream.

        :param predicate:
        """

    @abstractmethod
    def reduce(self, predicate: Callable[[_K, _K], _K], identity) -> _K:
        """
        Performs a reduction on the elements of this stream, using the provided identity value
        and an associative accumulation function, and returns the reduced value.

        :param predicate:
        :param identity:
        """

    @abstractmethod
    def all_match(self, predicate: Callable[[_K], bool]):
        """
        Returns whether all elements of this stream match the provided predicate.

        :param predicate: The callable predicate
        """

    def any_match(self, predicate: Callable[[_K], bool]):
        """
        Returns whether any elements of this stream match the provided predicate.

        :param predicate: The callable predicate
        """
        self._trigger_exec()
        return any(predicate(element) for element in self._source)

    def none_match(self, predicate: Callable[[_K], bool]):
        """
        Returns whether no elements of this stream match the provided predicate.

        :param predicate:
        """
        self._trigger_exec()
        return not any(predicate(element) for element in self._source)

    def min(self):
        """Returns the minimum element of this stream."""
        self._trigger_exec()
        if len(self._source) > 0:
            return Optional.of(min(self._source))
        return Optional.empty()

    def max(self):
        """Returns the maximum element of this stream."""
        self._trigger_exec()
        if len(self._source) > 0:
            return Optional.of(max(self._source))
        return Optional.empty()

    def find_first(self):
        """
        Returns an Optional describing the first element of this stream, or an empty Optional if
        the stream is empty. :return:
        """
        self._trigger_exec()
        if len(self._source) > 0:
            return Optional.of(self._source[0])
        return Optional.empty()

    def to_list(self):
        """Accumulates the elements of this stream into a List."""
        self._trigger_exec()
        return list(self._source)

    def to_tuple(self):
        """Accumulates the elements of this stream into a Tuple."""
        self._trigger_exec()
        return tuple(self._source)

    def to_set(self):
        """Accumulates the elements of this stream into a Set."""
        self._trigger_exec()
        return set(self._source)

    def count(self):
        """
        Returns the count of elements in this stream.

        :return: Number of elements in the stream
        """
        self._trigger_exec()
        return len(self._source)

    def _trigger_exec(self):
        self._queue.execute_all()
