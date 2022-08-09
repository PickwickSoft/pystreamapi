import itertools
from typing import Iterable, TypeVar, Callable, Optional

from pystreamapi.streams.__base_stream import BaseStream
from pystreamapi.streams.__parallel_stream import ParallelStream
from pystreamapi.streams.__sequential_stream import SequentialStream
from pystreamapi.__iterate import iterate

_K = TypeVar('_K')


class Stream:
    """The stream builder"""

    @staticmethod
    def of(source: Iterable[_K]) -> BaseStream[_K]:
        """
        Create a new Stream from a source. The implementation will decide whether to use a
        sequential or a parallel stream

        :param source:
        """
        return SequentialStream(source)

    @staticmethod
    def of_noneable(source: Optional[Iterable[_K]]) -> BaseStream[_K]:
        """
        Create a new Stream from a source. The implementation will decide whether to use a
        sequential or a parallel stream.

        If the source is None, an empty stream will be returned.

        :param source: The source to create the stream from. Can be None.
        """
        return Stream.of([]) if source is None else SequentialStream(source)

    @staticmethod
    def parallel_of(source: Iterable[_K]) -> BaseStream[_K]:
        """
        Create a parallel stream from a source

        :param source:
        """
        return ParallelStream(source)

    @staticmethod
    def sequential_of(source: Iterable[_K]) -> BaseStream[_K]:
        """
        Create a sequential stream from a source

        :param source:
        """
        return SequentialStream(source)

    @staticmethod
    def concat(*streams: "BaseStream[_K]"):
        """
        Creates a lazily concatenated stream whose elements are all the elements of the first stream
        followed by all the elements of the other streams.

        :param streams: The streams to concatenate
        :return: The concatenated stream
        """
        return streams[0].__class__(itertools.chain(*list(streams)))

    @staticmethod
    def iterate(seed: _K, func: Callable[[_K], _K]) -> BaseStream[_K]:
        """
        Returns an infinite sequential ordered Stream produced by iterative application of a
        function f to an initial element seed, producing a Stream consisting of seed,
        f(seed), f(f(seed)), etc.

        :param seed: The initial element
        :param func: The function to apply
        """
        return Stream.of(
            iterate(func, seed))
