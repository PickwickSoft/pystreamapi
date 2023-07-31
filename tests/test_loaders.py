import os
from unittest import TestCase

from pystreamapi.loaders import csv


class TestLoaders(TestCase):

    def setUp(self) -> None:
        cwd = os.path.dirname(os.path.realpath(__file__))
        self.path = os.path.join(cwd, 'assets')

    def test_csv_loader(self):
        data = csv(f'{self.path}/data.csv')
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0].attr1, 1)
        self.assertIsInstance(data[0].attr1, int)
        self.assertEqual(data[0].attr2, 2.0)
        self.assertIsInstance(data[0].attr2, float)
        self.assertEqual(data[1].attr1, 'a')
        self.assertIsInstance(data[1].attr1, str)

    def test_csv_loader_is_iterable(self):
        data = csv(f'{self.path}/data.csv')
        self.assertEqual(len(list(iter(data))), 2)

    def test_csv_loader_with_custom_delimiter(self):
        data = csv(f'{self.path}/data2.csv', delimiter=';')
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0].attr1, 1)
        self.assertIsInstance(data[0].attr1, int)

    def test_csv_loader_with_empty_file(self):
        data = csv(f'{self.path}/empty.csv')
        self.assertEqual(len(data), 0)

    def test_csv_loader_with_invalid_path(self):
        with self.assertRaises(FileNotFoundError):
            csv(f'{self.path}/invalid.csv')

    def test_csv_loader_with_non_absolute_path(self):
        with self.assertRaises(ValueError):
            csv('invalid.csv')
