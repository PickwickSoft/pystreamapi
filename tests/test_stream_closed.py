import unittest

from parameterized import parameterized_class

from pystreamapi._streams.__parallel_stream import ParallelStream
from pystreamapi._streams.__sequential_stream import SequentialStream
from pystreamapi._streams.numeric.__parallel_numeric_stream import ParallelNumericStream
from pystreamapi._streams.numeric.__sequential_numeric_stream import SequentialNumericStream


@parameterized_class("stream", [
    [SequentialStream],
    [ParallelStream],
    [SequentialNumericStream],
    [ParallelNumericStream]])
class BaseStreamClosed(unittest.TestCase):
    def test_closed_stream_throws_exception(self):
        closed_stream = self.stream([])
        closed_stream._close()

        # Verify that all methods throw a RuntimeError
        with self.assertRaises(RuntimeError):
            list(closed_stream)

        with self.assertRaises(RuntimeError):
            closed_stream.distinct()

        with self.assertRaises(RuntimeError):
            closed_stream.drop_while(lambda x: True)

        with self.assertRaises(RuntimeError):
            closed_stream.filter(lambda x: True)

        with self.assertRaises(RuntimeError):
            closed_stream.flat_map(lambda x: [x])

        with self.assertRaises(RuntimeError):
            closed_stream.group_by(lambda x: x)

        with self.assertRaises(RuntimeError):
            closed_stream.limit(5)

        with self.assertRaises(RuntimeError):
            closed_stream.map(lambda x: x)

        with self.assertRaises(RuntimeError):
            closed_stream.map_to_int()

        with self.assertRaises(RuntimeError):
            closed_stream.map_to_str()

        with self.assertRaises(RuntimeError):
            closed_stream.peek(lambda x: None)

        with self.assertRaises(RuntimeError):
            closed_stream.reversed()

        with self.assertRaises(RuntimeError):
            closed_stream.skip(5)

        with self.assertRaises(RuntimeError):
            closed_stream.sorted()

        with self.assertRaises(RuntimeError):
            closed_stream.take_while(lambda x: True)

        with self.assertRaises(RuntimeError):
            closed_stream.all_match(lambda x: True)

        with self.assertRaises(RuntimeError):
            closed_stream.any_match(lambda x: True)

        with self.assertRaises(RuntimeError):
            closed_stream.count()

        with self.assertRaises(RuntimeError):
            closed_stream.find_any()

        with self.assertRaises(RuntimeError):
            closed_stream.find_first()

        with self.assertRaises(RuntimeError):
            closed_stream.for_each(lambda x: None)

        with self.assertRaises(RuntimeError):
            closed_stream.none_match(lambda x: True)

        with self.assertRaises(RuntimeError):
            closed_stream.min()

        with self.assertRaises(RuntimeError):
            closed_stream.max()

        with self.assertRaises(RuntimeError):
            closed_stream.reduce(lambda x, y: x + y)

        with self.assertRaises(RuntimeError):
            closed_stream.to_list()

        with self.assertRaises(RuntimeError):
            closed_stream.to_tuple()

        with self.assertRaises(RuntimeError):
            closed_stream.to_set()

        with self.assertRaises(RuntimeError):
            closed_stream.to_dict(lambda x: x)