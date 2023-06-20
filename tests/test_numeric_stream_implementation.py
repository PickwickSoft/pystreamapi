from unittest import TestCase

from parameterized import parameterized_class

from pystreamapi._streams.numeric.__parallel_numeric_stream import ParallelNumericStream
from pystreamapi._streams.numeric.__sequential_numeric_stream import \
    SequentialNumericStream


@parameterized_class("stream", [
    [ParallelNumericStream],
    [SequentialNumericStream]])
class TestNumericStreamImplementation(TestCase):

    def test_mean(self):
        result = self.stream([1, 2, 3, 4, 5]).mean()
        self.assertEqual(result, 3)

    def test_mean_empty(self):
        result = self.stream([]).mean()
        self.assertEqual(result, None)

    def test_mean_negative(self):
        result = self.stream([-1, -2, -3, -4, -5]).mean()
        self.assertEqual(result, -3)

    def test_sum(self):
        result = self.stream([1, 2, 3, 4, 5]).sum()
        self.assertEqual(result, 15)

    def test_sum_empty(self):
        result = self.stream([]).sum()
        self.assertEqual(result, 0)
