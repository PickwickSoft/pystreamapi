# pylint: disable=wildcard-import,too-many-instance-attributes,unused-wildcard-import

import unittest

from pystreamapi.conditions import empty, not_empty, equal_to, not_equal_to
from pystreamapi.conditions.string import *


class TestStringConditions(unittest.TestCase):

    def test_empty(self):
        self.assertTrue(empty(''))
        self.assertFalse(empty('hello'))

    def test_not_empty(self):
        self.assertTrue(not_empty('hello'))
        self.assertFalse(not_empty(''))

    def test_contains(self):
        condition = contains('world')
        self.assertTrue(condition('hello world'))
        self.assertFalse(condition('hello'))

    def test_not_contains(self):
        condition = not_contains('world')
        self.assertTrue(condition('hello'))
        self.assertFalse(condition('hello world'))

    def test_starts_with(self):
        condition = starts_with('hello')
        self.assertTrue(condition('hello world'))
        self.assertFalse(condition('world hello'))

    def test_ends_with(self):
        condition = ends_with('world')
        self.assertTrue(condition('hello world'))
        self.assertFalse(condition('world hello'))

    def test_matches(self):
        condition = matches('^hello.*world$')
        self.assertTrue(condition('hello beautiful world'))
        self.assertFalse(condition('hello'))

    def test_not_matches(self):
        condition = not_matches('^hello.*world$')
        self.assertTrue(condition('hello'))
        self.assertFalse(condition('hello beautiful world'))

    def test_longer_than(self):
        condition = longer_than(5)
        self.assertTrue(condition('hello world'))
        self.assertFalse(condition('hello'))

    def test_shorter_than(self):
        condition = shorter_than(6)
        self.assertTrue(condition('hello'))
        self.assertFalse(condition('hello world'))

    def test_longer_than_or_equal(self):
        condition = longer_than_or_equal(5)
        self.assertTrue(condition('hello world'))
        self.assertTrue(condition('hello'))
        self.assertFalse(condition('he'))

    def test_shorter_than_or_equal(self):
        condition = shorter_than_or_equal(5)
        self.assertTrue(condition('hello'))
        self.assertTrue(condition('he'))
        self.assertFalse(condition('hello world'))

    def test_equal_to(self):
        condition = equal_to('hello')
        self.assertTrue(condition('hello'))
        self.assertFalse(condition('world'))

    def test_not_equal_to(self):
        condition = not_equal_to('hello')
        self.assertTrue(condition('world'))
        self.assertFalse(condition('hello'))

    def test_equal_to_ignore_case(self):
        condition = equal_to_ignore_case('HeLLo')
        self.assertTrue(condition('hello'))
        self.assertFalse(condition('world'))

    def test_not_equal_to_ignore_case(self):
        condition = not_equal_to_ignore_case('HeLLo')
        self.assertTrue(condition('world'))
        self.assertFalse(condition('hello'))

    def test_contains_ignore_case(self):
        condition = contains_ignore_case('WORLD')
        self.assertTrue(condition('hello world'))
        self.assertFalse(condition('hello'))

    def test_not_contains_ignore_case(self):
        condition = not_contains_ignore_case('WORLD')
        self.assertTrue(condition('hello'))
        self.assertFalse(condition('hello world'))

    def test_starts_with_ignore_case(self):
        condition = starts_with_ignore_case('HeLLo')
        self.assertTrue(condition('hello world'))
        self.assertFalse(condition('world hello'))

    def test_ends_with_ignore_case(self):
        condition = ends_with_ignore_case('WorLd')
        self.assertTrue(condition('hello world'))
        self.assertFalse(condition('world hello'))

    def test_matches_ignore_case(self):
        condition = matches_ignore_case('^heLLO.*worLD$')
        self.assertTrue(condition('hello beautiful world'))
        self.assertTrue(condition('HeLLo Beautiful WorlD'))
        self.assertFalse(condition('hello'))

    def test_not_matches_ignore_case(self):
        condition = not_matches_ignore_case('^heLLO.*worLD$')
        self.assertTrue(condition('hello'))
        self.assertFalse(condition('hello beautiful world'))
        self.assertFalse(condition('HeLLo Beautiful WorlD'))
