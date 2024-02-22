from unittest import TestCase

from pystreamapi import Stream
from pystreamapi.conditions import prime


class TestParallelStream(TestCase):
    def test_parallel(self):
        # success 0
        (Stream.of(range(10)).parallel()
         .map(lambda x: x * 2)
         .for_each(print))

        # success 1
        (Stream.parallel_of(range(10))
         .map(lambda x: x * 2)
         .filter(prime())
         .for_each(print))

        # failed
        (Stream.of(range(10)).parallel()
         .map(lambda x: x * 2)
         .filter(prime())
         .for_each(print))
