import unittest

from pystreamapi._itertools.tools import reduce, dropwhile


class TestReduce(unittest.TestCase):
    def test_reduce_with_empty_sequence_and_no_initial_value(self):
        with self.assertRaises(TypeError) as cm:
            reduce(lambda x, y: x + y, [], handler=None)
        self.assertEqual(
            str(cm.exception),
            "reduce() of empty iterable with no initial value"
        )

    def test_reduce_with_empty_sequence_and_initial_value(self):
        result = reduce(lambda x, y: x + y, [], initial=10, handler=None)
        self.assertEqual(result, 10)

    def test_reduce_with_sequence_and_no_initial_value(self):
        sequence = [1, 2, 3, 4, 5]
        result = reduce(lambda x, y: x + y, sequence, handler=None)
        self.assertEqual(result, 15)

    def test_reduce_with_sequence_and_initial_value(self):
        sequence = [1, 2, 3, 4, 5]
        result = reduce(lambda x, y: x + y, sequence, initial=10, handler=None)
        self.assertEqual(result, 25)


class TestDropWhile(unittest.TestCase):
    def test_dropwhile_with_empty_iterable(self):
        iterable = []
        result = list(dropwhile(lambda x: x < 5, iterable, handler=None))
        self.assertEqual(result, [])

    def test_dropwhile_with_non_empty_iterable(self):
        iterable = [1, 2, 3, 4, 5, 6, 7]
        result = list(dropwhile(lambda x: x < 5, iterable, handler=None))
        self.assertEqual(result, [5, 6, 7])
