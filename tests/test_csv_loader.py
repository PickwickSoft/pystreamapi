# pylint: disable=not-context-manager
from unittest import TestCase
from unittest.mock import patch, mock_open

from file_test import OPEN, PATH_EXISTS, PATH_ISFILE
from pystreamapi.loaders import csv

file_content = """
attr1,attr2
1,2.0
a,b
"""
file_path = 'path/to/data.csv'


class TestCSVLoader(TestCase):

    def test_csv_loader(self):
        with (patch(OPEN, mock_open(read_data=file_content)),
              patch(PATH_EXISTS, return_value=True),
              patch(PATH_ISFILE, return_value=True)):
            data = csv(file_path)
            self.assertEqual(len(data), 2)
            self.assertEqual(data[0].attr1, 1)
            self.assertIsInstance(data[0].attr1, int)
            self.assertEqual(data[0].attr2, 2.0)
            self.assertIsInstance(data[0].attr2, float)
            self.assertEqual(data[1].attr1, 'a')
            self.assertIsInstance(data[1].attr1, str)

    def test_csv_loader_with_casting_disabled(self):
        with (patch(OPEN, mock_open(read_data=file_content)),
              patch(PATH_EXISTS, return_value=True),
              patch(PATH_ISFILE, return_value=True)):
            data = csv(file_path, cast_types=False)
            self.assertEqual(len(data), 2)
            self.assertEqual(data[0].attr1, '1')
            self.assertIsInstance(data[0].attr1, str)
            self.assertEqual(data[0].attr2, '2.0')
            self.assertIsInstance(data[0].attr2, str)
            self.assertEqual(data[1].attr1, 'a')
            self.assertIsInstance(data[1].attr1, str)

    def test_csv_loader_is_iterable(self):
        with (patch(OPEN, mock_open(read_data=file_content)),
              patch(PATH_EXISTS, return_value=True),
              patch(PATH_ISFILE, return_value=True)):
            data = csv(file_path)
            self.assertEqual(len(list(iter(data))), 2)

    def test_csv_loader_with_custom_delimiter(self):
        with (patch(OPEN, mock_open(read_data=file_content.replace(",", ";"))),
              patch(PATH_EXISTS, return_value=True),
              patch(PATH_ISFILE, return_value=True)):
            data = csv(file_path, delimiter=';')
            self.assertEqual(len(data), 2)
            self.assertEqual(data[0].attr1, 1)
            self.assertIsInstance(data[0].attr1, int)

    def test_csv_loader_with_empty_file(self):
        with (patch(OPEN, mock_open(read_data="")),
              patch(PATH_EXISTS, return_value=True),
              patch(PATH_ISFILE, return_value=True)):
            data = csv(file_path)
            self.assertEqual(len(data), 0)

    def test_csv_loader_with_invalid_path(self):
        with self.assertRaises(FileNotFoundError):
            csv('path/to/invalid.csv')

    def test_csv_loader_with_no_file(self):
        with self.assertRaises(ValueError):
            csv('./')
