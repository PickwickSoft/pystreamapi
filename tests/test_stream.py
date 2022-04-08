import unittest

from pystreamapi.stream import Stream


class TestStream(unittest.TestCase):

    def test_stream_sort_unsorted(self):
        result = Stream([3, 2, 9, 1]).sorted().to_list()
        self.assertListEqual(result, [1, 2, 3, 9])

    def test_stream_sort_sorted(self):
        result = Stream([1, 2, 3, 9]).sorted().to_list()
        self.assertListEqual(result, [1, 2, 3, 9])

    def test_stream_for_each(self):
        result = Stream([1, 2, 3, 9]).for_each(str).to_list()
        self.assertListEqual(result, ["1", "2", "3", "9"])

    def test_map_str_to_int(self):
        result = Stream(["1", "2", "3", "9"]).map(int).to_list()
        self.assertListEqual(result, [1, 2, 3, 9])

    def test_filter_not_none(self):
        result = Stream([1, 2, "3", None]).filter(lambda x: x is not None).to_list()
        self.assertListEqual(result, [1, 2, "3"])

    def test_filter_str(self):
        result = Stream([1, 2, "3", None]).filter(lambda x: type(x) == str).to_list()
        self.assertListEqual(result, ["3"])

    def test_count(self):
        result = Stream([1, 2, "3", None]).count()
        self.assertEqual(result, 4)

    def test_reduce(self):
        src = [1, 2, 3, 4, 5]
        result = Stream(src).reduce(lambda x, y: x + y)
        self.assertEqual(result, sum(src))


if __name__ == '__main__':
    unittest.main()
