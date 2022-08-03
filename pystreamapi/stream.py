from typing import Iterable

from pystreamapi.streams.__parallel_stream import ParallelStream
from pystreamapi.streams.__sequential_stream import SequentialStream
from pystreamapi.streams.__base_stream import BaseStream


class Stream:

    @staticmethod
    def of(source: Iterable) -> BaseStream:
        return SequentialStream(source)

    @staticmethod
    def parallel_of(source: Iterable) -> BaseStream:
        return ParallelStream(source)

    @staticmethod
    def sequential_of(source: Iterable) -> BaseStream:
        return SequentialStream(source)
