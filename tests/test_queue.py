from unittest import TestCase

from helper import TestHelper
from pystreamapi.lazy.process import Process
from pystreamapi.lazy.queue import ProcessQueue


class TestProcessQueue(TestCase):
    def test_append(self):
        process = Process(print, 1)
        queue = ProcessQueue()
        self.assertListEqual(queue.get_queue(), [])
        queue.append(process)
        self.assertListEqual(queue.get_queue(), [process])

    def test_execute_all(self):
        helper = TestHelper()
        process = Process(helper.increment, 1)
        queue = ProcessQueue()
        self.assertEqual(helper.value, 0)
        queue.append(process)
        queue.execute_all()
        self.assertEqual(helper.value, 1)

    def test_execute_all_multiple_processes(self):
        helper = TestHelper()
        process = Process(helper.increment, 1)
        queue = ProcessQueue()
        self.assertEqual(helper.value, 0)
        queue.append(process)
        queue.append(process)
        queue.append(process)
        queue.execute_all()
        self.assertEqual(helper.value, 3)
