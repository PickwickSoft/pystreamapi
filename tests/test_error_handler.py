# pylint: disable=protected-access
from unittest import TestCase

from pystreamapi._streams.error.__error import ErrorHandler, _sentinel
from pystreamapi._streams.error.__sentinel import Sentinel
from pystreamapi._streams.error.__levels import ErrorLevel


class ErrorHandlerImpl(ErrorHandler):
    pass

class TestErrorLevelMeta(TestCase):

    def setUp(self) -> None:
        self.handler = ErrorHandlerImpl()

    def test_iterate_raise(self):
        self.handler.error_level(ErrorLevel.RAISE)
        self.assertRaises(ValueError, lambda: self.handler._itr([1, 2, 3, 4, 5, "a"], int))

    def test_iterate_raise_with_condition(self):
        self.handler.error_level(ErrorLevel.RAISE)
        self.assertRaises(ValueError, lambda: self.handler._itr(
            [1, 2, 3, 4, 5, "a"], int, lambda x: x != ""))

    def test_iterate_ignore(self):
        self.handler.error_level(ErrorLevel.IGNORE)
        self.assertEqual(self.handler._itr([1, 2, 3, 4, 5, "a"], int), [1, 2, 3, 4, 5])

    def test_iterate_ignore_with_condition(self):
        self.handler.error_level(ErrorLevel.IGNORE)
        self.assertEqual(self.handler._itr(
            [1, 2, 3, 4, 5, "a"], int, lambda x: x != ""), [1, 2, 3, 4, 5])


    def test_iterate_ignore_specific_exceptions(self):
        self.handler.error_level(ErrorLevel.IGNORE, ValueError, AttributeError)
        self.assertEqual(self.handler._itr(
            ["b", 2, 3, 4, 5, "a"], mapper=lambda x: x.split()), [["b"], ["a"]])


    def test_iterate_ignore_specific_exception_raise_another(self):
        self.handler.error_level(ErrorLevel.IGNORE, ValueError)
        self.assertRaises(AttributeError, lambda: self.handler._itr(
            ["b", 2, 3, 4, 5, "a"], mapper=lambda x: x.split()))

    def test_iterate_warn(self):
        self.handler.error_level(ErrorLevel.WARN)
        self.assertEqual(self.handler._itr([1, 2, 3, 4, 5, "a"], int), [1, 2, 3, 4, 5])

    def test_iterate_warn_with_condition(self):
        self.handler.error_level(ErrorLevel.WARN)
        self.assertEqual(self.handler._itr(
            [1, 2, 3, 4, 5, "a"], int, lambda x: x != ""), [1, 2, 3, 4, 5])

    def test_one_raise(self):
        self.handler.error_level(ErrorLevel.RAISE)
        self.assertRaises(ValueError, lambda: self.handler._one(mapper=int, item="a"))

    def test_one_raise_with_condition(self):
        self.handler.error_level(ErrorLevel.RAISE)
        self.assertRaises(ValueError, lambda: self.handler._one(int, lambda x: x != "",
                                                                "a"))

    def test_one_condition_false(self):
        self.handler.error_level(ErrorLevel.RAISE)
        self.assertEqual(self.handler._one(int, lambda x: x == "", "1"), _sentinel)

    def test_one_ignore(self):
        self.handler.error_level(ErrorLevel.IGNORE)
        self.assertEqual(self.handler._one(mapper=int, item="a"), _sentinel)

    def test_one_ignore_with_condition(self):
        self.handler.error_level(ErrorLevel.IGNORE)
        self.assertEqual(self.handler._one(int, lambda x: x != "", "a"), _sentinel)

    def test_one_ignore_specific_exceptions(self):
        self.handler.error_level(ErrorLevel.IGNORE, ValueError, AttributeError)
        self.assertEqual(self.handler._one(
            mapper=lambda x: x.split(), item=1), _sentinel)

    def test_one_ignore_specific_exception_raise_another(self):
        self.handler.error_level(ErrorLevel.IGNORE, ValueError)
        self.assertRaises(AttributeError, lambda: self.handler._one(
            mapper=lambda x: x.split(), item=1))

    def test_one_warn(self):
        self.handler.error_level(ErrorLevel.WARN)
        self.assertEqual(self.handler._one(mapper=int, item="a"), _sentinel)

    def test_one_warn_with_condition(self):
        self.handler.error_level(ErrorLevel.WARN)
        self.assertEqual(self.handler._one(int, lambda x: x != "", "a"), _sentinel)

    def test_remove_sentinels(self):
        self.handler.error_level(ErrorLevel.IGNORE)
        src = ["1", 2, "3", "a"]
        self.assertEqual(self.handler._remove_sentinel(
            self.handler._one(mapper=int, item=item) for item in src),
            [1, 2, 3]
        )

    def test_remove_sentinels_no_sentinels(self):
        self.handler.error_level(ErrorLevel.IGNORE)
        src = ["1", 2, "3", "a"]
        self.assertEqual(self.handler._remove_sentinel(src), src)

    def test_sentinel_eq(self):
        s1 = Sentinel()
        s2 = Sentinel()
        self.assertTrue(s1 == s2)

    def test_sentinel_eq_false(self):
        s1 = Sentinel()
        s2 = object()
        self.assertFalse(s1 == s2)

    def test_sentinel_ne(self):
        s1 = Sentinel()
        s2 = object()
        self.assertTrue(s1 != s2)

    def test_sentinel_ne_false(self):
        s1 = Sentinel()
        s2 = Sentinel()
        self.assertFalse(s1 != s2)

    def test_sentinel_hash(self):
        s1 = Sentinel()
        s2 = Sentinel()
        self.assertEqual(hash(s1), hash(s2))
        self.assertEqual(hash(s1), 0)
