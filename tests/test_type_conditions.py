# pylint: disable=wildcard-import,too-many-instance-attributes,unused-wildcard-import

import unittest
from pystreamapi.conditions.types import *


class TestFilters(unittest.TestCase):

    def test_of_type(self):
        filter_func = of_type(int)
        self.assertTrue(filter_func(10))
        self.assertFalse(filter_func("10"))

    def test_not_of_type(self):
        filter_func = not_of_type(int)
        self.assertFalse(filter_func(10))
        self.assertTrue(filter_func("10"))

    def test_none(self):
        filter_func = none
        self.assertTrue(filter_func()(None))
        self.assertFalse(filter_func()(0))

    def test_not_none(self):
        filter_func = not_none
        self.assertFalse(filter_func()(None))
        self.assertTrue(filter_func()(0))

    def test_true(self):
        filter_func = true
        self.assertTrue(filter_func()(True))
        self.assertFalse(filter_func()(False))

    def test_not_true(self):
        filter_func = not_true
        self.assertFalse(filter_func()(True))
        self.assertTrue(filter_func()(False))

    def test_false(self):
        filter_func = false
        self.assertTrue(filter_func()(False))
        self.assertFalse(filter_func()(True))

    def test_not_false(self):
        filter_func = not_false
        self.assertFalse(filter_func()(False))
        self.assertTrue(filter_func()(True))

    def test_length(self):
        filter_func = length
        self.assertTrue(filter_func(3)("123"))
        self.assertFalse(filter_func(3)("1234"))

    def test_not_length(self):
        filter_func = not_length
        self.assertTrue(filter_func(3)("1234"))
        self.assertFalse(filter_func(3)("123"))

    def test_empty(self):
        filter_func = empty
        self.assertTrue(filter_func()(""))
        self.assertFalse(filter_func()("123"))

    def test_not_empty(self):
        filter_func = not_empty
        self.assertTrue(filter_func()("123"))
        self.assertFalse(filter_func()(""))

    def test_equal(self):
        filter_func = equal(10)
        self.assertTrue(filter_func(10))
        self.assertFalse(filter_func(20))

    def test_not_equal(self):
        filter_func = not_equal(10)
        self.assertFalse(filter_func(10))
        self.assertTrue(filter_func(20))
