import unittest

from pystreamapi.conditions.combiners import one_of


class TestCombinersConditions(unittest.TestCase):

    def test_returns_true_if_any_condition_is_true(self):
        def is_even(x):
            return x % 2 == 0

        def is_positive(x):
            return x > 0

        any_even_or_positive = one_of(is_even, is_positive)

        self.assertTrue(any_even_or_positive(4))
        self.assertTrue(any_even_or_positive(7))
        self.assertTrue(any_even_or_positive(-2))
        self.assertTrue(any_even_or_positive(0))

    def test_returns_false_if_all_conditions_are_false(self):
        def is_even(x):
            return x % 2 == 0

        def is_positive(x):
            return x > 0

        any_even_or_positive = one_of(is_even, is_positive)

        self.assertFalse(any_even_or_positive(-3))
        self.assertFalse(any_even_or_positive(-1))
