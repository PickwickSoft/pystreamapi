from typing import Iterator
from unittest import TestCase
from pystreamapi.__iterate import iterate


class TestIterateFunctions(TestCase):
    def test_iterate(self):
        self.assertIsInstance(iterate(lambda x: x + 1, 0), Iterator)
