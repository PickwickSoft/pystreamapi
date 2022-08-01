import unittest
from functools import reduce as seq_reduce
from pystreamapi.parallel.itertools import reduce, pfilter


class TestParallelFunctions(unittest.TestCase):

    def test_reduce(self):
        result = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
        self.assertEqual(result, 15)

    def test_reduce_empty(self):
        result = reduce(lambda x, y: x + y, [])
        self.assertEqual(result, [])

    def test_reduce_one_element(self):
        result = reduce(lambda x, y: x + y, [1])
        self.assertEqual(result, [1])

    def test_reduce_big_source(self):
        result = reduce(lambda x, y: x + y, list(range(1000)))
        self.assertEqual(result, 499_500)

    def test_parallel_vs_sequential_reduce(self):
        parallel = reduce(lambda x, y: x + y, list(range(1000)))
        sequential = seq_reduce(lambda x, y: x + y, list(range(1000)))
        self.assertEqual(parallel, sequential)

    def test_filter(self):
        result = pfilter([1, 2, "3", None], lambda x: x is not None)
        self.assertListEqual([1, 2, "3"], result)

    def test_filter_empty(self):
        result = pfilter([], lambda x: x is not None)
        self.assertListEqual([], result)

    def test_filter_one(self):
        result = pfilter([None], lambda x: x is not None)
        self.assertListEqual([], result)
