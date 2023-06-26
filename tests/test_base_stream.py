import unittest

from pystreamapi.__optional import Optional

from pystreamapi.__stream import Stream
from pystreamapi._streams.__parallel_stream import ParallelStream
from pystreamapi._streams.__sequential_stream import SequentialStream
from pystreamapi._streams.numeric.__sequential_numeric_stream import SequentialNumericStream


class TestBaseStream(unittest.TestCase):

    def test_concat(self):
        result = Stream.concat(Stream.of([1, 2, 3]), Stream.of([9, 10, 11]))
        self.assertListEqual(result.to_list(), [1, 2, 3, 9, 10, 11])

    def test_concat_empty(self):
        result = Stream.concat(Stream.of([]), Stream.of([1, 2, 3, 9]))
        self.assertListEqual(result.to_list(), [1, 2, 3, 9])

    def test_concat_empty_empty(self):
        result = Stream.concat(Stream.of([]), Stream.of([])).to_list()
        self.assertListEqual(result, [])

    def test_concat_unsorted(self):
        result = Stream.concat(Stream.of([9, 6, 1]), Stream.of([3, 5, 99]))
        self.assertListEqual(result.to_list(), [9, 6, 1, 3, 5, 99])

    def test_iterate(self):
        result = Stream.iterate(1, lambda x: x + 1).limit(3).to_list()
        self.assertListEqual(result, [1, 2, 3])

    def test_iterate_empty(self):
        result = Stream.iterate(1, lambda x: x + 1).limit(0).to_list()
        self.assertListEqual(result, [])

    def test_of_parallel(self):
        stream = Stream.parallel_of([1, 2])
        self.assertIsInstance(stream, ParallelStream)

    def test_of_sequential(self):
        stream = Stream.sequential_of([1, 2])
        self.assertIsInstance(stream, SequentialStream)

    def test_of_numeric(self):
        stream = Stream.of([1, 2])
        self.assertIsInstance(stream, SequentialNumericStream)

    def test_of_non_numeric(self):
        stream = Stream.of(["1", "2"])
        self.assertIsInstance(stream, SequentialStream)

    def test_of_noneable_none(self):
        result = Stream.of_noneable(None).to_list()
        self.assertListEqual(result, [])

    def test_of_noneable_valid(self):
        result = Stream.of_noneable([1, 2, 3]).to_list()
        self.assertListEqual(result, [1, 2, 3])

    def test_concat_after_initialization(self):
        stream1 = Stream.of([1, 2, 3])
        stream2 = Stream.of([4, 5, 6])
        stream3 = Stream.of([7, 8, 9])
        result = stream1.concat(stream2, stream3).to_list()
        self.assertListEqual(result, [4, 5, 6, 7, 8, 9])

    def test_sort_unsorted(self):
        result = Stream.of([3, 2, 9, 1]).sorted().to_list()
        self.assertListEqual(result, [1, 2, 3, 9])

    def test_sort_sorted(self):
        result = Stream.of([1, 2, 3, 9]).sorted().to_list()
        self.assertListEqual(result, [1, 2, 3, 9])

    @staticmethod
    def compare(a, b):
        return b - a

    def test_sort_comparator_unsorted(self):
        result = Stream.of([1, 2, 3, 9]).sorted(self.compare).to_list()
        self.assertListEqual(result, [9, 3, 2, 1])

    def test_sort_comparator_sorted(self):
        result = Stream.of([9, 3, 2, 1]).sorted(self.compare).to_list()
        self.assertListEqual(result, [9, 3, 2, 1])

    def test_reversed(self):
        result = Stream.of([1, 2, 3, 9]).reversed().to_list()
        self.assertListEqual(result, [9, 3, 2, 1])

    def test_reversed_unsorted(self):
        result = Stream.of([2, 1, 9, 6]).reversed().to_list()
        self.assertListEqual(result, [6, 9, 1, 2])

    def test_reversed_empty(self):
        result = Stream.of([]).reversed().to_list()
        self.assertListEqual(result, [])

    def test_reversed_wrong_type(self):
        def finite_generator():
            index = 1
            while index < 5:
                yield index
                index += 1

        result = Stream.of(finite_generator()).reversed().to_list()
        self.assertListEqual(result, [4, 3, 2, 1])

    def test_limit(self):
        result = Stream.of([1, 2, 3, 9]).limit(3).to_list()
        self.assertListEqual(result, [1, 2, 3])

    def test_limit_empty(self):
        result = Stream.of([]).limit(3).to_list()
        self.assertListEqual(result, [])

    def test_skip(self):
        result = Stream.of([1, 2, 3, 9]).skip(2).to_list()
        self.assertListEqual(result, [3, 9])

    def test_skip_empty(self):
        result = Stream.of([]).skip(2).to_list()
        self.assertListEqual(result, [])

    def test_distinct(self):
        result = Stream.of([1, 2, 3, 9, 1, 2, 3, 9]).distinct().to_list()
        self.assertListEqual(result, [1, 2, 3, 9])

    def test_distinct_empty(self):
        result = Stream.of([]).distinct().to_list()
        self.assertListEqual(result, [])

    def test_drop_while(self):
        result = Stream.of([1, 2, 3, 9]).drop_while(lambda x: x < 3).to_list()
        self.assertListEqual(result, [3, 9])

    def test_drop_while_empty(self):
        result = Stream.of([]).drop_while(lambda x: x < 3).to_list()
        self.assertListEqual(result, [])

    def test_take_while(self):
        result = Stream.of([1, 2, 3, 9]).take_while(lambda x: x < 3).to_list()
        self.assertListEqual(result, [1, 2])

    def test_take_while_empty(self):
        result = Stream.of([]).take_while(lambda x: x < 3).to_list()
        self.assertListEqual(result, [])

    def test_count(self):
        result = Stream.of([1, 2, "3", None]).count()
        self.assertEqual(result, 4)

    def test_any_match(self):
        result = Stream.of([1, 2, 3, 9]).any_match(lambda x: x > 3)
        self.assertTrue(result)

    def test_any_match_empty(self):
        result = Stream.of([]).any_match(lambda x: x > 3)
        self.assertFalse(result)

    def test_none_match(self):
        result = Stream.of([1, 2, 3, 9]).none_match(lambda x: x > 3)
        self.assertFalse(result)

    def test_none_match_empty(self):
        result = Stream.of([]).none_match(lambda x: x > 3)
        self.assertTrue(result)

    def test_min(self):
        result = Stream.of([1, 2, 3, 9]).filter(lambda x: x > 2).min()
        self.assertEqual(result, Optional.of(3))

    def test_min_empty(self):
        result = Stream.of([]).min()
        self.assertEqual(result, Optional.empty())

    def test_max(self):
        result = Stream.of([1, 2, 3, 9]).filter(lambda x: x < 5).max()
        self.assertEqual(result, Optional.of(3))

    def test_max_empty(self):
        result = Stream.of([]).max()
        self.assertEqual(result, Optional.empty())

    def test_find_first(self):
        result = Stream.of([1, 2, 3, 9]).find_first()
        self.assertEqual(result, Optional.of(1))

    def test_find_first_empty(self):
        result = Stream.of([]).find_first()
        self.assertEqual(result, Optional.empty())

    def test_to_tuple(self):
        result = Stream.of([1, 2, 3, 9]).to_tuple()
        self.assertTupleEqual(result, (1, 2, 3, 9))

    def test_to_set(self):
        result = Stream.of([1, 2, 3, 9]).to_set()
        self.assertSetEqual(result, {1, 2, 3, 9})


if __name__ == '__main__':
    unittest.main()
