import unittest

from _lazy.helper import TestHelper
from pystreamapi._lazy.process import Process


class TestProcess(unittest.TestCase):

    def test_exec_with_args(self):
        helper = TestHelper()
        process = Process(helper.increment, 1)
        self.assertEqual(helper.value, 0)
        process.exec()
        self.assertEqual(helper.value, 1)

    def test_exec_no_args(self):
        helper = TestHelper()
        process = Process(helper.increment)
        self.assertEqual(helper.value, 0)
        process.exec()
        self.assertEqual(helper.value, 0)
