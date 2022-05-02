from typing import Iterable

from pystreamapi.streams.__sequential_stream import SequentialStream


class Stream:

    @staticmethod
    def of(source: Iterable):
        return SequentialStream(source)
