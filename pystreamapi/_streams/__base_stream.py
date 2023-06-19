import itertools
from abc import abstractmethod
from builtins import reversed
from functools import cmp_to_key
from typing import Iterable, Callable, Any, TypeVar, Iterator, Union

from optional import Optional
from optional.nothing import Nothing
from optional.something import Something

from pystreamapi._lazy.process import Process
from pystreamapi._lazy.queue import ProcessQueue

K = TypeVar('K')
_V = TypeVar('_V')
_identity_missing = object()


class BaseStream(Iterable[K]):
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

    def __init__(self, source: Iterable[K]):
        self._source = source
        self._queue = ProcessQueue()

    def __iter__(self) -> Iterator[K]:
        self._trigger_exec()
        return iter(self._source)

    @classmethod
    def concat(cls, *streams: "BaseStream[K]"):
        """
        Creates a lazily concatenated stream whose elements are all the elements of the first stream
        followed by all the elements of the other streams.

        :param streams: The streams to concatenate
        :return: The concatenated stream
        """
        return cls(itertools.chain(*list(streams)))

    def distinct(self) -> 'BaseStream[_V]':
        """Returns a stream consisting of the distinct elements of this stream."""
        self._queue.append(Process(self.__distinct))
        return self

    def __distinct(self):
        """Removes duplicate elements from the stream."""
        self._source = list(set(self._source))

    def drop_while(self, predicate: Callable[[K], bool]) -> 'BaseStream[_V]':
        """
        Returns, if this stream is ordered, a stream consisting of the remaining elements of this
        stream after dropping the longest prefix of elements that match the given predicate.

        :param predicate:
        """
        self._queue.append(Process(self.__drop_while, predicate))
        return self

    def __drop_while(self, predicate: Callable[[Any], bool]):
        """Drops elements from the stream while the predicate is true."""
        self._source = list(itertools.dropwhile(predicate, self._source))

    def filter(self, predicate: Callable[[K], bool]) -> 'BaseStream[K]':
        """
        Returns a stream consisting of the elements of this stream that match the given predicate.

        :param predicate:
        """
        self._queue.append(Process(self._filter, predicate))
        return self

    @abstractmethod
    def _filter(self, predicate: Callable[[K], bool]):
        """Implementation of filter. Should be implemented by subclasses."""

    def flat_map(self, predicate: Callable[[K], Iterable[_V]]) -> 'BaseStream[_V]':
        """
        Returns a stream consisting of the results of replacing each element of this stream with
        the contents of a mapped stream produced by applying the provided mapping function to
        each element.

        :param predicate:
        """
        self._queue.append(Process(self._flat_map, predicate))
        return self

    @abstractmethod
    def _flat_map(self, predicate: Callable[[K], Iterable[_V]]):
        """Implementation of flat_map. Should be implemented by subclasses."""

    def group_by(self, key_mapper: Callable[[K], Any]) -> 'BaseStream[K]':
        """
        Returns a Stream consisting of the results of grouping the elements of this stream
        by the given classifier and extracting the key/value pairs.

        :param key_mapper:
        """
        self._queue.append(Process(self.__group_by, key_mapper))
        return self

    def __group_by(self, key_mapper: Callable[[Any], Any]):
        groups = self._group_to_dict(key_mapper)
        self._source = groups.items()

    @abstractmethod
    def _group_to_dict(self, key_mapper: Callable[[K], Any]) -> dict[K, list]:
        """Groups the stream into a dictionary. Should be implemented by subclasses."""

    def limit(self, max_size: int) -> 'BaseStream[_V]':
        """
        Returns a stream consisting of the elements of this stream, truncated to be no longer
        than maxSize in length.

        :param max_size:
        """
        self._queue.append(Process(self.__limit, max_size))
        return self

    def __limit(self, max_size: int):
        """Limits the stream to the first n elements."""
        self._source = itertools.islice(self._source, max_size)

    def map(self, mapper: Callable[[K], _V]) -> 'BaseStream[_V]':
        """
        Returns a stream consisting of the results of applying the given function to the elements
        of this stream.

        :param mapper:
        """
        self._queue.append(Process(self._map, mapper))
        return self

    @abstractmethod
    def _map(self, mapper: Callable[[K], _V]):
        """Implementation of map. Should be implemented by subclasses."""

    def map_to_int(self) -> 'BaseStream[_V]':
        """
        Returns a stream consisting of the results of converting the elements of this stream to
        integers.
        """
        self._queue.append(Process(self.__map_to_int))
        return self

    def __map_to_int(self):
        self._map(int)

    def map_to_str(self) -> 'BaseStream[_V]':
        """
        Returns a stream consisting of the results of converting the elements of this stream to
        strings.
        """
        self._queue.append(Process(self.__map_to_str))
        return self

    def __map_to_str(self):
        self._map(str)

    def peek(self, action: Callable) -> 'BaseStream[_V]':
        """
        Returns a stream consisting of the elements of this stream, additionally performing the
        provided action on each element as elements are consumed from the resulting stream.

        :param action:
        """
        self._queue.append(Process(self._peek, action))
        return self

    @abstractmethod
    def _peek(self, action: Callable):
        """Implementation of peek. Should be implemented by subclasses."""

    def reversed(self) -> 'BaseStream[_V]':
        """
        Returns a stream consisting of the elements of this stream, with their order being
        reversed.
        """
        self._queue.append(Process(self.__reversed))
        return self

    def __reversed(self):
        """Reverses the stream."""
        try:
            self._source = reversed(self._source)
        except TypeError:
            self._source = reversed(list(self._source))

    def skip(self, n: int) -> 'BaseStream[_V]':
        """
        Returns a stream consisting of the remaining elements of this stream after discarding the
        first n elements of the stream.

        :param n:
        """
        self._queue.append(Process(self.__skip, n))
        return self

    def __skip(self, n: int):
        """Skips the first n elements of the stream."""
        self._source = self._source[n:]

    def sorted(self, comparator: Callable[[K], int] = None) -> 'BaseStream[_V]':
        """
        Returns a stream consisting of the elements of this stream, sorted according to natural
        order.
        """
        self._queue.append(Process(self.__sorted, comparator))
        return self

    def __sorted(self, comparator: Callable[[K], int] = None):
        """Sorts the stream."""
        if comparator is None:
            self._source = sorted(self._source)
        else:
            self._source = sorted(self._source, key=cmp_to_key(comparator))

    def take_while(self, predicate: Callable[[K], bool]) -> 'BaseStream[_V]':
        """
        Returns, if this stream is ordered, a stream consisting of the longest prefix of elements
        taken from this stream that match the given predicate.

        :param predicate:
        """
        self._queue.append(Process(self.__take_while, predicate))
        return self

    def __take_while(self, predicate: Callable[[Any], bool]):
        """Takes elements from the stream while the predicate is true."""
        self._source = list(itertools.takewhile(predicate, self._source))

    # Terminal Operations:

    @abstractmethod
    def all_match(self, predicate: Callable[[K], bool]):
        """
        Returns whether all elements of this stream match the provided predicate.

        :param predicate: The callable predicate
        """

    def any_match(self, predicate: Callable[[K], bool]):
        """
        Returns whether any elements of this stream match the provided predicate.

        :param predicate: The callable predicate
        """
        self._trigger_exec()
        return any(predicate(element) for element in self._source)

    def count(self):
        """
        Returns the count of elements in this stream.

        :return: Number of elements in the stream
        """
        self._trigger_exec()
        return len(self._source)

    @abstractmethod
    def find_any(self) -> Optional:
        """
        Returns an Optional describing some element of the stream, or an empty Optional if the
        stream is empty.
        """

    def find_first(self):
        """
        Returns an Optional describing the first element of this stream, or an empty Optional if
        the stream is empty. :return:
        """
        self._trigger_exec()
        if len(self._source) > 0:
            return Optional.of(self._source[0])
        return Optional.empty()

    @abstractmethod
    def for_each(self, predicate: Callable):
        """
        Performs an action for each element of this stream.

        :param predicate:
        """

    def none_match(self, predicate: Callable[[K], bool]):
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

    @abstractmethod
    def reduce(self, predicate: Callable[[K, K], K], identity=_identity_missing,
               depends_on_state=False) -> Union[K, Something, Nothing]:
        """
        Performs a reduction on the elements of this stream, using the provided identity value
        and an associative accumulation function, and returns the reduced value.

        :param depends_on_state: Weather processing order changes result or not
        :param predicate:
        :param identity: Default value
        """

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

    @abstractmethod
    def to_dict(self, key_mapper: Callable[[K], Any]) -> dict:
        """
        Returns a dictionary consisting of the results of grouping the elements of this stream
        by the given classifier.

        :param key_mapper:
        """

    def _trigger_exec(self):
        """Triggers execution of the stream."""
        self._queue.execute_all()
