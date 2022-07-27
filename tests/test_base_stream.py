import unittest

from optional import Optional
from optional.something import Something

from pystreamapi.stream import Stream


class TestBaseStream(unittest.TestCase):

    def test_sort_unsorted(self):
        result = Stream.of([3, 2, 9, 1]).sorted().to_list()
        self.assertListEqual(result, [1, 2, 3, 9])

    def test_sort_sorted(self):
        result = Stream.of([1, 2, 3, 9]).sorted().to_list()
        self.assertListEqual(result, [1, 2, 3, 9])

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

    def test_reduce_no_identity(self):
        src = [1, 2, 3, 4, 5]
        result = Stream.of(src).reduce(lambda x, y: x + y)
        self.assertEqual(type(result), Something)
        self.assertEqual(result.get_or_default("Empty"), sum(src))

    def test_reduce_with_identity(self):
        src = [1, 2, 3, 4, 5]
        result = Stream.of(src).reduce(lambda x, y: x + y, identity=0)
        self.assertEqual(type(result), int)
        self.assertEqual(result, sum(src))

    def test_reduce_empty_stream_no_identity(self):
        result = Stream.of([]).reduce(lambda x, y: x + y)
        self.assertEqual(result, Optional.empty())

    def test_reduce_empty_stream_with_identity(self):
        result = Stream.of([]).reduce(lambda x, y: x + y, identity=0)
        self.assertEqual(result, 0)

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
