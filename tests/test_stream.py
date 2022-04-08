import unittest

from pystreamapi.stream import Stream


class TestStream(unittest.TestCase):

    def test_sort_unsorted(self):
        result = Stream([3, 2, 9, 1]).sorted().to_list()
        self.assertListEqual(result, [1, 2, 3, 9])

    def test_sort_sorted(self):
        result = Stream([1, 2, 3, 9]).sorted().to_list()
        self.assertListEqual(result, [1, 2, 3, 9])

    def test_for_each(self):
        out = []
        Stream([1, 2, 3, 9]).for_each(out.append)
        self.assertListEqual(out, [1, 2, 3, 9])

    def test_map_str_to_int(self):
        result = Stream(["1", "2", "3", "9"]).map(int).to_list()
        self.assertListEqual(result, [1, 2, 3, 9])

    def test_map_str_to_int_then_str(self):
        result = Stream(["1", "2", "3", "9"]).map(int).map(str).to_list()
        self.assertListEqual(result, ["1", "2", "3", "9"])

    def test_filter_not_none(self):
        result = Stream([1, 2, "3", None]).filter(lambda x: x is not None).to_list()
        self.assertListEqual(result, [1, 2, "3"])

    def test_filter_str(self):
        result = Stream([1, 2, "3", None]).filter(lambda x: isinstance(x, str)).to_list()
        self.assertListEqual(result, ["3"])

    def test_count(self):
        result = Stream([1, 2, "3", None]).count()
        self.assertEqual(result, 4)

    def test_reduce(self):
        src = [1, 2, 3, 4, 5]
        result = Stream(src).reduce(lambda x, y: x + y)
        self.assertEqual(result, sum(src))

    def test_lazy_filter(self):
        result = Stream([" ", '3', None, "2", 1, ""]) \
            .filter(lambda x: x is not None) \
            .map(str) \
            .map(lambda x: x.strip()) \
            .filter(lambda x: len(x) > 0) \
            .map(int) \
            .sorted() \
            .to_list()
        self.assertListEqual(result, [1, 2, 3])

    def test_peek(self):
        src = []
        result = Stream(["1", "2", "3", "9"]).map(int).peek(lambda x: src.append(x)).map(str).to_list()
        self.assertListEqual(result, ["1", "2", "3", "9"])
        self.assertListEqual(src, [1, 2, 3, 9])


if __name__ == '__main__':
    unittest.main()
