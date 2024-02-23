from unittest import TestCase

from pystreamapi import Stream
from pystreamapi.conditions import prime


class TestParallelStream(TestCase):
    def test_parallel(self):
        # success
        (Stream.of(range(10)).parallel()
         .map(lambda x: x * 2)
         .for_each(print))

        # success
        (Stream.parallel_of(range(10))
         .map(lambda x: x * 2)
         .filter(prime())
         .for_each(print))

        # fail -> fixed
        (Stream.of(range(10)).parallel()
         .map(lambda x: x * 2)
         .filter(prime())
         .for_each(print))
