from typing import Iterable, TypeVar

from pystreamapi.streams.__base_stream import BaseStream
from pystreamapi.streams.__parallel_stream import ParallelStream
from pystreamapi.streams.__sequential_stream import SequentialStream

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
