import unittest

from optional import Optional
from optional.something import Something
from parameterized import parameterized_class
from pystreamapi.streams.__parallel_stream import ParallelStream
from pystreamapi.streams.__sequential_stream import SequentialStream
from pystreamapi.streams.__base_stream import BaseStream


@parameterized_class("stream", [
    [SequentialStream],
    [ParallelStream]])
class TestStreamImplementation(unittest.TestCase):

    def test_for_each(self):
        out = []
        self.stream([1, 2, 3, 9]).for_each(out.append)
        self.assertListEqual(out, [1, 2, 3, 9])

    def test_map_str_to_int(self):
        result = self.stream(["1", "2", "3", "9"]).map(int).to_list()
        self.assertListEqual(result, [1, 2, 3, 9])

    def test_map_str_to_int_then_str(self):
        result = self.stream(["1", "2", "3", "9"]).map(int).map(str).to_list()
        self.assertListEqual(result, ["1", "2", "3", "9"])

    def test_map_to_int(self):
        result = self.stream(["1", "2", "3", "9"]).map_to_int().to_list()
        self.assertListEqual(result, [1, 2, 3, 9])

    def test_map_to_int_empty(self):
        result = self.stream([]).map_to_int().to_list()
        self.assertListEqual(result, [])

    def test_map_to_str(self):
        result = self.stream([1, 2, 3, 9]).map_to_str().to_list()
        self.assertListEqual(result, ["1", "2", "3", "9"])

    def test_flat_map(self):
        result = self.stream([1, 2, 3, 9]).flat_map(lambda x: self.stream([x, x])).to_list()
        self.assertListEqual(result, [1, 1, 2, 2, 3, 3, 9, 9])

    def test_filter_not_none(self):
        result = self.stream([1, 2, "3", None]).filter(lambda x: x is not None).to_list()
        self.assertListEqual(result, [1, 2, "3"])

    def test_filter_str(self):
        result = self.stream([1, 2, "3", None]).filter(lambda x: isinstance(x, str)).to_list()
        self.assertListEqual(result, ["3"])

    def test_filter_complex(self):
        result = self.stream([" ", '3', None, "2", 1, ""]) \
            .filter(lambda x: x is not None) \
            .map(str) \
            .map(lambda x: x.strip()) \
            .filter(lambda x: len(x) > 0) \
            .map(int) \
            .sorted() \
            .to_list()
        self.assertListEqual(result, [1, 2, 3])

    def test_filter_lazy(self):
        result = self.stream([1, 2, 3]).filter(lambda x: x > 1)
        self.assertListEqual(result.to_list(), [2, 3])
        self.assertTrue(isinstance(result, BaseStream))

    def test_peek(self):
        src = []
        result = self.stream(["1", "2", "3", "9"]).map(int).peek(src.append).map(str).to_list()
        self.assertListEqual(result, ["1", "2", "3", "9"])
        self.assertListEqual(src, [1, 2, 3, 9])

    def test_all_match(self):
        result = self.stream([1, 2, 3, 9]).all_match(lambda x: x > 0)
        self.assertTrue(result)
        result = self.stream([1, 2, 3, 9]).all_match(lambda x: x > 1)
        self.assertFalse(result)

    def test_all_match_empty(self):
        result = self.stream([]).all_match(lambda x: x > 0)
        self.assertTrue(result)

    def test_find_any(self):
        result = self.stream([1, 2, 3, 9]).find_any()
        self.assertEqual(result, Optional.of(1))

    def test_find_any_empty(self):
        result = self.stream([]).find_any()
        self.assertEqual(result, Optional.empty())

    def test_limit(self):
        result = self.stream([1, 2, 3, 9]).limit(2).to_list()
        self.assertListEqual(result, [1, 2])

    def test_limit_empty(self):
        result = self.stream([]).limit(2).to_list()
        self.assertListEqual(result, [])

    def test_reduce_no_identity(self):
        src = [1, 2, 3, 4, 5]
        result = self.stream(src).reduce(lambda x, y: x + y)
        self.assertEqual(type(result), Something)
        self.assertEqual(result.get_or_default("Empty"), sum(src))

    def test_reduce_with_identity(self):
        src = [1, 2, 3, 4, 5]
        result = self.stream(src).reduce(lambda x, y: x + y, identity=0)
        self.assertEqual(type(result), int)
        self.assertEqual(result, sum(src))

    def test_reduce_empty_stream_no_identity(self):
        result = self.stream([]).reduce(lambda x, y: x + y)
        self.assertEqual(result, Optional.empty())

    def test_reduce_empty_stream_with_identity(self):
        result = self.stream([]).reduce(lambda x, y: x + y, identity=0)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
