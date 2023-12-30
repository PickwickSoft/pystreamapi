from unittest import TestCase

from pystreamapi._streams.numeric.__sequential_numeric_stream import \
    SequentialNumericStream as Stream


class TestNumericBaseStream(TestCase):
    def test_range(self):
        result = Stream([1, 2, 3, 4, 5]).range()
        self.assertEqual(result, 4)

    def test_range_empty(self):
        result = Stream([]).range()
        self.assertIsNone(result)

    def test_range_negative(self):
        result = Stream([-1, -2, -3, -4, -5]).range()
        self.assertEqual(result, 4)

    def test_interquartile_range(self):
        result = Stream([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).interquartile_range()
        self.assertEqual(result, 5)

    def test_interquartile_range_empty(self):
        result = Stream([]).interquartile_range()
        self.assertIsNone(result)

    def test_interquartile_range_odd(self):
        result = Stream([1, 2, 3, 4, 5, 6, 7, 8, 9]).interquartile_range()
        self.assertEqual(result, 5)

    def test_median(self):
        result = Stream([1, 2, 3, 4, 5]).median()
        self.assertEqual(result, 3)

    def test_median_even(self):
        result = Stream([1, 2, 3, 4, 5, 6]).median()
        self.assertEqual(result, 3.5)

    def test_median_empty(self):
        result = Stream([]).median()
        self.assertIsNone(result)

    def test_first_quartile(self):
        result = Stream([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).first_quartile()
        self.assertEqual(result, 3)

    def test_first_quartile_empty(self):
        result = Stream([]).first_quartile()
        self.assertIsNone(result)

    def test_first_quartile_odd(self):
        result = Stream([1, 2, 3, 4, 5, 6, 7, 8, 9]).first_quartile()
        self.assertEqual(result, 2.5)

    def test_third_quartile(self):
        result = Stream([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).third_quartile()
        self.assertEqual(result, 8)

    def test_third_quartile_empty(self):
        result = Stream([]).third_quartile()
        self.assertIsNone(result)

    def test_third_quartile_odd(self):
        result = Stream([1, 2, 3, 4, 5, 6, 7, 8, 9]).third_quartile()
        self.assertEqual(result, 7.5)

    def test_mode(self):
        result = Stream([1, 2, 3, 4, 4]).mode()
        self.assertEqual(result, [4])

    def test_mode_multiple(self):
        result = Stream([1, 2, 3, 3, 4, 4]).mode()
        self.assertEqual(result, [3, 4])

    def test_mode_empty(self):
        result = Stream([]).mode()
        self.assertIsNone(result)

    def test_mode_negative(self):
        result = Stream([-1, -2, -3, -3]).mode()
        self.assertEqual(result, [-3])
